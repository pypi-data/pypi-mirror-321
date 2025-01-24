import json
import logging
import sys
import traceback
from functools import wraps

import flask
from flasgger import Swagger
from flask import Flask, Response, jsonify, request
from flask_sock import Sock

from ..base import VannaBase
from ._cache import Cache, MemoryCache
from .auth import AuthInterface, NoAuth


class VannaFlaskAPI:
    flask_app = None

    def requires_cache(self, required_fields, optional_fields=[]):
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                id = request.args.get('id')

                if id is None:
                    id = request.json.get('id')
                    if id is None:
                        return jsonify({'type': 'error', 'error': 'No id provided'})

                for field in required_fields:
                    if self.cache.get(id=id, field=field) is None:
                        return jsonify({'type': 'error', 'error': f'No {field} found'})

                field_values = {
                    field: self.cache.get(id=id, field=field)
                    for field in required_fields
                }

                for field in optional_fields:
                    field_values[field] = self.cache.get(id=id, field=field)

                # Add the id to the field_values
                field_values['id'] = id

                return f(*args, **field_values, **kwargs)

            return decorated

        return decorator

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            user = self.auth.get_user(flask.request)

            if not self.auth.is_logged_in(user):
                return jsonify(
                    {'type': 'not_logged_in', 'html': self.auth.login_form()}
                )

            # Pass the user to the function
            return f(*args, user=user, **kwargs)

        return decorated

    def __init__(
        self,
        vn: VannaBase,
        cache: Cache = MemoryCache(),
        auth: AuthInterface = NoAuth(),
        debug=True,
        allow_llm_to_see_data=False,
        chart=True,
        port: int = 8000,
    ):
        """
        Expose a Flask API that can be used to interact with a Vanna instance.

        Args:
            vn: The Vanna instance to interact with.
            cache: The cache to use. Defaults to MemoryCache, which uses an in-memory cache. You can also pass in a custom cache that implements the Cache interface.
            auth: The authentication method to use. Defaults to NoAuth, which doesn't require authentication. You can also pass in a custom authentication method that implements the AuthInterface interface.
            debug: Show the debug console. Defaults to True.
            allow_llm_to_see_data: Whether to allow the LLM to see data. Defaults to False.
            chart: Whether to show the chart output in the UI. Defaults to True.

        Returns:
            None
        """
        self._port = port
        self.flask_app = Flask(__name__)

        self.swagger = Swagger(
            self.flask_app, template={'info': {'title': 'Vanna API'}}
        )
        self.sock = Sock(self.flask_app)
        self.ws_clients = []
        self.vn = vn
        self.auth = auth
        self.cache = cache
        self.debug = debug
        self.allow_llm_to_see_data = allow_llm_to_see_data
        self.chart = chart
        self.config = {
            'debug': debug,
            'allow_llm_to_see_data': allow_llm_to_see_data,
            'chart': chart,
        }
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        if 'google.colab' in sys.modules:
            self.debug = False
            print(
                "Google Colab doesn't support running websocket servers. Disabling debug mode."
            )

        if self.debug:

            def log(message, title='Info'):
                [
                    ws.send(json.dumps({'message': message, 'title': title}))
                    for ws in self.ws_clients
                ]

            self.vn.log = log

        @self.flask_app.route('/api/v0/get_config', methods=['GET'])
        @self.requires_auth
        def get_config(user: any):
            """
            Get the configuration for a user
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: config
                    config:
                      type: object
            """
            config = self.auth.override_config_for_user(user, self.config)
            return jsonify({'type': 'config', 'config': config})

        @self.flask_app.route('/api/v0/generate_questions', methods=['GET'])
        @self.requires_auth
        def generate_questions(user: any):
            """
            Generate questions
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_list
                    questions:
                      type: array
                      items:
                        type: string
                    header:
                      type: string
                      default: Here are some questions you can ask
            """
            # If self has an _model attribute and model=='chinook'
            if hasattr(self.vn, '_model') and self.vn._model == 'chinook':
                return jsonify(
                    {
                        'type': 'question_list',
                        'questions': [
                            'What are the top 10 artists by sales?',
                            'What are the total sales per year by country?',
                            'Who is the top selling artist in each genre? Show the sales numbers.',
                            'How do the employees rank in terms of sales performance?',
                            'Which 5 cities have the most customers?',
                        ],
                        'header': 'Here are some questions you can ask:',
                    }
                )

            training_data = vn.get_training_data()

            # If training data is None or empty
            if training_data is None or len(training_data) == 0:
                return jsonify(
                    {
                        'type': 'error',
                        'error': 'No training data found. Please add some training data first.',
                    }
                )

            # Get the questions from the training data
            try:
                # Filter training data to only include questions where the question is not null
                questions = (
                    training_data[training_data['question'].notnull()]
                    .sample(5)['question']
                    .tolist()
                )

                # Temporarily this will just return an empty list
                return jsonify(
                    {
                        'type': 'question_list',
                        'questions': questions,
                        'header': 'Here are some questions you can ask',
                    }
                )
            except Exception as e:
                return jsonify(
                    {
                        'type': 'question_list',
                        'questions': [],
                        'header': 'Go ahead and ask a question',
                    }
                )

        @self.flask_app.route('/api/v0/generate_sql', methods=['GET'])
        @self.requires_auth
        def generate_sql(user: any):
            """
            Generate SQL from a question
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: query
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            question = flask.request.args.get('question')

            if question is None:
                return jsonify({'type': 'error', 'error': 'No question provided'})

            id = self.cache.generate_id(question=question)
            sql = vn.generate_sql(
                question=question, allow_llm_to_see_data=self.allow_llm_to_see_data
            )

            self.cache.set(id=id, field='question', value=question)
            self.cache.set(id=id, field='sql', value=sql)

            if vn.is_sql_valid(sql=sql):
                return jsonify(
                    {
                        'type': 'sql',
                        'id': id,
                        'text': sql,
                    }
                )
            else:
                return jsonify(
                    {
                        'type': 'text',
                        'id': id,
                        'text': sql,
                    }
                )

        @self.flask_app.route('/api/v0/generate_rewritten_question', methods=['GET'])
        @self.requires_auth
        def generate_rewritten_question(user: any):
            """
            Generate a rewritten question
            ---
            parameters:
              - name: last_question
                in: query
                type: string
                required: true
              - name: new_question
                in: query
                type: string
                required: true
            """

            last_question = flask.request.args.get('last_question')
            new_question = flask.request.args.get('new_question')

            rewritten_question = self.vn.generate_rewritten_question(
                last_question, new_question
            )

            return jsonify(
                {'type': 'rewritten_question', 'question': rewritten_question}
            )

        @self.flask_app.route('/api/v0/get_function', methods=['GET'])
        @self.requires_auth
        def get_function(user: any):
            """
            Get a function from a question
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: query
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: function
                    id:
                      type: object
                    function:
                      type: string
            """
            question = flask.request.args.get('question')

            if question is None:
                return jsonify({'type': 'error', 'error': 'No question provided'})

            if not hasattr(vn, 'get_function'):
                return jsonify(
                    {
                        'type': 'error',
                        'error': 'This setup does not support function generation.',
                    }
                )

            id = self.cache.generate_id(question=question)
            function = vn.get_function(question=question)

            if function is None:
                return jsonify({'type': 'error', 'error': 'No function found'})

            if 'instantiated_sql' not in function:
                self.vn.log(f'No instantiated SQL found for {question} in {function}')
                return jsonify({'type': 'error', 'error': 'No instantiated SQL found'})

            self.cache.set(id=id, field='question', value=question)
            self.cache.set(id=id, field='sql', value=function['instantiated_sql'])

            if (
                'instantiated_post_processing_code' in function
                and function['instantiated_post_processing_code'] is not None
                and len(function['instantiated_post_processing_code']) > 0
            ):
                self.cache.set(
                    id=id,
                    field='plotly_code',
                    value=function['instantiated_post_processing_code'],
                )

            return jsonify(
                {
                    'type': 'function',
                    'id': id,
                    'function': function,
                }
            )

        @self.flask_app.route('/api/v0/get_all_functions', methods=['GET'])
        @self.requires_auth
        def get_all_functions(user: any):
            """
            Get all the functions
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: functions
                    functions:
                      type: array
            """
            if not hasattr(vn, 'get_all_functions'):
                return jsonify(
                    {
                        'type': 'error',
                        'error': 'This setup does not support function generation.',
                    }
                )

            functions = vn.get_all_functions()

            return jsonify(
                {
                    'type': 'functions',
                    'functions': functions,
                }
            )

        @self.flask_app.route('/api/v0/run_sql', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['sql'])
        def run_sql(user: any, id: str, sql: str):
            """
            Run SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: df
                    id:
                      type: string
                    df:
                      type: object
                    should_generate_chart:
                      type: boolean
            """
            if not vn.run_sql_is_set:
                return jsonify(
                    {
                        'type': 'error',
                        'error': 'Please connect to a database using vn.connect_to_... in order to run SQL queries.',
                    }
                )
            try:
                df = vn.run_sql(sql=sql)
            except Exception:
                return jsonify(
                    {
                        'type': 'sql_error',
                        'error': str(
                            traceback.format_exc() + '\nthis was generated in run_sql'
                        ),
                    }
                )
            try:
                self.cache.set(id=id, field='df', value=df)

            except Exception as e:
                return jsonify(
                    {
                        'type': 'sql_error',
                        'error': str(
                            traceback.format_exc()
                            + '\nthis was generated in cache set dataframe'
                        ),
                    }
                )

            return jsonify(
                {
                    'type': 'df',
                    'id': id,
                    'df': df.head(10).to_json(orient='records', date_format='iso'),
                    'should_generate_chart': self.chart
                    and vn.should_generate_chart(df),
                }
            )

        @self.flask_app.route('/api/v0/fix_sql', methods=['POST'])
        @self.requires_auth
        @self.requires_cache(['question', 'sql'])
        def fix_sql(user: any, id: str, question: str, sql: str):
            """
            Fix SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: error
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            error = flask.request.json.get('error')

            if error is None:
                return jsonify({'type': 'error', 'error': 'No error provided'})

            question = f'I have an error: {error}\n\nHere is the SQL I tried to run: {sql}\n\nThis is the question I was trying to answer: {question}\n\nCan you rewrite the SQL to fix the error?'

            fixed_sql = vn.generate_sql(question=question)

            self.cache.set(id=id, field='sql', value=fixed_sql)

            return jsonify(
                {
                    'type': 'sql',
                    'id': id,
                    'text': fixed_sql,
                }
            )

        @self.flask_app.route('/api/v0/update_sql', methods=['POST'])
        @self.requires_auth
        @self.requires_cache([])
        def update_sql(user: any, id: str):
            """
            Update SQL
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: sql
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: sql
                    id:
                      type: string
                    text:
                      type: string
            """
            sql = flask.request.json.get('sql')

            if sql is None:
                return jsonify({'type': 'error', 'error': 'No sql provided'})

            self.cache.set(id=id, field='sql', value=sql)

            return jsonify(
                {
                    'type': 'sql',
                    'id': id,
                    'text': sql,
                }
            )

        @self.flask_app.route('/api/v0/download_csv', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['df'])
        def download_csv(user: any, id: str, df):
            """
            Download CSV
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                description: download CSV
            """
            csv = df.to_csv()

            return Response(
                csv,
                mimetype='text/csv',
                headers={'Content-disposition': f'attachment; filename={id}.csv'},
            )

        @self.flask_app.route('/api/v0/generate_plotly_figure', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['df', 'question', 'sql'])
        def generate_plotly_figure(user: any, id: str, df, question, sql):
            """
            Generate plotly figure
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
              - name: chart_instructions
                in: body
                type: string
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: plotly_figure
                    id:
                      type: string
                    fig:
                      type: object
            """
            chart_instructions = flask.request.args.get('chart_instructions')

            try:
                # If chart_instructions is not set then attempt to retrieve the code from the cache
                if chart_instructions is None or len(chart_instructions) == 0:
                    code = self.cache.get(id=id, field='plotly_code')
                else:
                    question = f'{question}. When generating the chart, use these special instructions: {chart_instructions}'
                    code = vn.generate_plotly_code(
                        question=question,
                        sql=sql,
                        df_metadata=f'Running df.dtypes gives:\n {df.dtypes}',
                    )
                    self.cache.set(id=id, field='plotly_code', value=code)

                fig = vn.get_plotly_figure(plotly_code=code, df=df, dark_mode=False)
                fig_json = fig.to_json()

                self.cache.set(id=id, field='fig_json', value=fig_json)

                return jsonify(
                    {
                        'type': 'plotly_figure',
                        'id': id,
                        'fig': fig_json,
                    }
                )
            except Exception as e:
                # Print the stack trace
                import traceback

                traceback.print_exc()

                return jsonify({'type': 'error', 'error': str(e)})

        @self.flask_app.route('/api/v0/get_training_data', methods=['GET'])
        @self.requires_auth
        def get_training_data(user: any):
            """
            Get all training data
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: df
                    id:
                      type: string
                      default: training_data
                    df:
                      type: object
            """
            df = vn.get_training_data()

            if df is None or len(df) == 0:
                return jsonify(
                    {
                        'type': 'error',
                        'error': 'No training data found. Please add some training data first.',
                    }
                )

            return jsonify(
                {
                    'type': 'df',
                    'id': 'training_data',
                    'df': df.to_json(orient='records'),
                }
            )

        @self.flask_app.route('/api/v0/remove_training_data', methods=['POST'])
        @self.requires_auth
        def remove_training_data(user: any):
            """
            Remove training data
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            # Get id from the JSON body
            id = flask.request.json.get('id')

            if id is None:
                return jsonify({'type': 'error', 'error': 'No id provided'})

            if vn.remove_training_data(id=id):
                return jsonify({'success': True})
            else:
                return jsonify(
                    {'type': 'error', 'error': "Couldn't remove training data"}
                )

        @self.flask_app.route('/api/v0/train', methods=['POST'])
        @self.requires_auth
        def add_training_data(user: any):
            """
            Add training data
            ---
            parameters:
              - name: user
                in: query
              - name: question
                in: body
                type: string
              - name: sql
                in: body
                type: string
              - name: ddl
                in: body
                type: string
              - name: documentation
                in: body
                type: string
            responses:
              200:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
            """
            question = flask.request.json.get('question')
            sql = flask.request.json.get('sql')
            ddl = flask.request.json.get('ddl')
            documentation = flask.request.json.get('documentation')

            try:
                id = vn.train(
                    question=question, sql=sql, ddl=ddl, documentation=documentation
                )

                return jsonify({'id': id})
            except Exception as e:
                print('TRAINING ERROR', e)
                return jsonify({'type': 'error', 'error': str(e)})

        @self.flask_app.route('/api/v0/create_function', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['question', 'sql'])
        def create_function(user: any, id: str, question: str, sql: str):
            """
            Create function
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: function_template
                    id:
                      type: string
                    function_template:
                      type: object
            """
            plotly_code = self.cache.get(id=id, field='plotly_code')

            if plotly_code is None:
                plotly_code = ''

            function_data = self.vn.create_function(
                question=question, sql=sql, plotly_code=plotly_code
            )

            return jsonify(
                {
                    'type': 'function_template',
                    'id': id,
                    'function_template': function_data,
                }
            )

        @self.flask_app.route('/api/v0/update_function', methods=['POST'])
        @self.requires_auth
        def update_function(user: any):
            """
            Update function
            ---
            parameters:
              - name: user
                in: query
              - name: old_function_name
                in: body
                type: string
                required: true
              - name: updated_function
                in: body
                type: object
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            old_function_name = flask.request.json.get('old_function_name')
            updated_function = flask.request.json.get('updated_function')

            print('old_function_name', old_function_name)
            print('updated_function', updated_function)

            updated = vn.update_function(
                old_function_name=old_function_name, updated_function=updated_function
            )

            return jsonify({'success': updated})

        @self.flask_app.route('/api/v0/delete_function', methods=['POST'])
        @self.requires_auth
        def delete_function(user: any):
            """
            Delete function
            ---
            parameters:
              - name: user
                in: query
              - name: function_name
                in: body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    success:
                      type: boolean
            """
            function_name = flask.request.json.get('function_name')

            return jsonify({'success': vn.delete_function(function_name=function_name)})

        @self.flask_app.route('/api/v0/generate_followup_questions', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['df', 'question', 'sql'])
        def generate_followup_questions(user: any, id: str, df, question, sql):
            """
            Generate followup questions
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_list
                    questions:
                      type: array
                      items:
                        type: string
                    header:
                      type: string
            """
            if self.allow_llm_to_see_data:
                followup_questions = vn.generate_followup_questions(
                    question=question, sql=sql, df=df
                )
                if followup_questions is not None and len(followup_questions) > 5:
                    followup_questions = followup_questions[:5]

                self.cache.set(
                    id=id, field='followup_questions', value=followup_questions
                )

                return jsonify(
                    {
                        'type': 'question_list',
                        'id': id,
                        'questions': followup_questions,
                        'header': 'Here are some potential followup questions:',
                    }
                )
            else:
                self.cache.set(id=id, field='followup_questions', value=[])
                return jsonify(
                    {
                        'type': 'question_list',
                        'id': id,
                        'questions': [],
                        'header': 'Followup Questions can be enabled if you set allow_llm_to_see_data=True',
                    }
                )

        @self.flask_app.route('/api/v0/generate_summary', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(['df', 'question'])
        def generate_summary(user: any, id: str, df, question):
            """
            Generate summary
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: text
                    id:
                      type: string
                    text:
                      type: string
            """
            if self.allow_llm_to_see_data:
                summary = vn.generate_summary(question=question, df=df)

                self.cache.set(id=id, field='summary', value=summary)

                return jsonify(
                    {
                        'type': 'text',
                        'id': id,
                        'text': summary,
                    }
                )
            else:
                return jsonify(
                    {
                        'type': 'text',
                        'id': id,
                        'text': 'Summarization can be enabled if you set allow_llm_to_see_data=True',
                    }
                )

        @self.flask_app.route('/api/v0/load_question', methods=['GET'])
        @self.requires_auth
        @self.requires_cache(
            ['question', 'sql', 'df'], optional_fields=['summary', 'fig_json']
        )
        def load_question(user: any, id: str, question, sql, df, fig_json, summary):
            """
            Load question
            ---
            parameters:
              - name: user
                in: query
              - name: id
                in: query|body
                type: string
                required: true
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_cache
                    id:
                      type: string
                    question:
                      type: string
                    sql:
                      type: string
                    df:
                      type: object
                    fig:
                      type: object
                    summary:
                      type: string
            """
            try:
                return jsonify(
                    {
                        'type': 'question_cache',
                        'id': id,
                        'question': question,
                        'sql': sql,
                        'df': df.head(10).to_json(orient='records', date_format='iso'),
                        'fig': fig_json,
                        'summary': summary,
                    }
                )

            except Exception as e:
                return jsonify({'type': 'error', 'error': str(e)})

        @self.flask_app.route('/api/v0/get_question_history', methods=['GET'])
        @self.requires_auth
        def get_question_history(user: any):
            """
            Get question history
            ---
            parameters:
              - name: user
                in: query
            responses:
              200:
                schema:
                  type: object
                  properties:
                    type:
                      type: string
                      default: question_history
                    questions:
                      type: array
                      items:
                        type: string
            """
            return jsonify(
                {
                    'type': 'question_history',
                    'questions': cache.get_all(field_list=['question']),
                }
            )

        @self.flask_app.route('/api/v0/<path:catch_all>', methods=['GET', 'POST'])
        def catch_all(catch_all):
            return jsonify(
                {'type': 'error', 'error': 'The rest of the API is not ported yet.'}
            )

        if self.debug:

            @self.sock.route('/api/v0/log')
            def sock_log(ws):
                self.ws_clients.append(ws)

                try:
                    while True:
                        message = (
                            ws.receive()
                        )  # This example just reads and ignores to keep the socket open
                finally:
                    self.ws_clients.remove(ws)

    def run(self, *args, **kwargs):
        """
        Run the Flask app.

        Args:
            *args: Arguments to pass to Flask's run method.
            **kwargs: Keyword arguments to pass to Flask's run method.

        Returns:
            None
        """
        if args or kwargs:
            self.flask_app.run(*args, **kwargs)

        else:
            try:
                from google.colab import output

                output.serve_kernel_port_as_window(8084)
                from google.colab.output import eval_js

                print('Your app is running at:')
                print(eval_js('google.colab.kernel.proxyPort(8084)'))
            except:
                print('Your app is running at:')
                print(f'http://localhost:{self._port}')

            self.flask_app.run(
                host='0.0.0.0', port=self._port, debug=self.debug, use_reloader=False
            )
