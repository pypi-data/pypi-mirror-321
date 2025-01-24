import os
import pathlib

import flask
from flask import Response, send_from_directory

from itsai.aspire.vanna.flask._cache import Cache, DuckdbCache

from ..base import VannaBase
from ._api import VannaFlaskAPI
from .assets import css_content, html_content, js_content
from .auth import AuthInterface, NoAuth

_DB_PATH = pathlib.Path('cache.duckdb')


class VannaFlaskApp(VannaFlaskAPI):
    def __init__(
        self,
        vn: VannaBase,
        cache: Cache = DuckdbCache(_DB_PATH),
        auth: AuthInterface = NoAuth(),
        debug=True,
        allow_llm_to_see_data=False,
        logo='https://img.vanna.ai/vanna-flask.svg',
        title='Welcome to Vanna.AI',
        subtitle='Your AI-powered copilot for SQL queries.',
        show_training_data=True,
        suggested_questions=True,
        sql=True,
        table=True,
        csv_download=True,
        chart=True,
        redraw_chart=True,
        auto_fix_sql=True,
        ask_results_correct=True,
        followup_questions=True,
        summarization=True,
        function_generation=True,
        index_html_path=None,
        assets_folder=None,
        port: int = 8000,
    ):
        """
        Expose a Flask app that can be used to interact with a Vanna instance.

        Args:
            vn: The Vanna instance to interact with.
            cache: The cache to use. Defaults to MemoryCache, which uses an in-memory cache. You can also pass in a custom cache that implements the Cache interface.
            auth: The authentication method to use. Defaults to NoAuth, which doesn't require authentication. You can also pass in a custom authentication method that implements the AuthInterface interface.
            debug: Show the debug console. Defaults to True.
            allow_llm_to_see_data: Whether to allow the LLM to see data. Defaults to False.
            logo: The logo to display in the UI. Defaults to the Vanna logo.
            title: The title to display in the UI. Defaults to "Welcome to Vanna.AI".
            subtitle: The subtitle to display in the UI. Defaults to "Your AI-powered copilot for SQL queries.".
            show_training_data: Whether to show the training data in the UI. Defaults to True.
            suggested_questions: Whether to show suggested questions in the UI. Defaults to True.
            sql: Whether to show the SQL input in the UI. Defaults to True.
            table: Whether to show the table output in the UI. Defaults to True.
            csv_download: Whether to allow downloading the table output as a CSV file. Defaults to True.
            chart: Whether to show the chart output in the UI. Defaults to True.
            redraw_chart: Whether to allow redrawing the chart. Defaults to True.
            auto_fix_sql: Whether to allow auto-fixing SQL errors. Defaults to True.
            ask_results_correct: Whether to ask the user if the results are correct. Defaults to True.
            followup_questions: Whether to show followup questions. Defaults to True.
            summarization: Whether to show summarization. Defaults to True.
            index_html_path: Path to the index.html. Defaults to None, which will use the default index.html
            assets_folder: The location where you'd like to serve the static assets from. Defaults to None, which will use hardcoded Python variables.

        Returns:
            None
        """
        super().__init__(vn, cache, auth, debug, allow_llm_to_see_data, chart, port)

        self.config['logo'] = logo
        self.config['title'] = title
        self.config['subtitle'] = subtitle
        self.config['show_training_data'] = show_training_data
        self.config['suggested_questions'] = suggested_questions
        self.config['sql'] = sql
        self.config['table'] = table
        self.config['csv_download'] = csv_download
        self.config['chart'] = chart
        self.config['redraw_chart'] = redraw_chart
        self.config['auto_fix_sql'] = auto_fix_sql
        self.config['ask_results_correct'] = ask_results_correct
        self.config['followup_questions'] = followup_questions
        self.config['summarization'] = summarization
        self.config['function_generation'] = function_generation and hasattr(
            vn, 'get_function'
        )
        # self.config["version"] = importlib.metadata.version('vanna')

        self.index_html_path = index_html_path
        self.assets_folder = assets_folder

        @self.flask_app.route('/auth/login', methods=['POST'])
        def login():
            return self.auth.login_handler(flask.request)

        @self.flask_app.route('/auth/callback', methods=['GET'])
        def callback():
            return self.auth.callback_handler(flask.request)

        @self.flask_app.route('/auth/logout', methods=['GET'])
        def logout():
            return self.auth.logout_handler(flask.request)

        @self.flask_app.route('/assets/<path:filename>')
        def proxy_assets(filename):
            if self.assets_folder:
                return send_from_directory(self.assets_folder, filename)

            if '.css' in filename:
                return Response(css_content, mimetype='text/css')

            if '.js' in filename:
                return Response(js_content, mimetype='text/javascript')

            # Return 404
            return 'File not found', 404

        # Proxy the /vanna.svg file to the remote server
        @self.flask_app.route('/vanna.svg')
        def proxy_vanna_svg():
            return 'no file', 404

        @self.flask_app.route('/', defaults={'path': ''})
        @self.flask_app.route('/<path:path>')
        def hello(path: str):
            if self.index_html_path:
                directory = os.path.dirname(self.index_html_path)
                filename = os.path.basename(self.index_html_path)
                return send_from_directory(directory=directory, path=filename)
            return html_content
