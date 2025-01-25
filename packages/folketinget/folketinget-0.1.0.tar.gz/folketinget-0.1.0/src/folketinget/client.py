import requests
import urllib

class Folketinget:
    """Client for the Folketinget API."""

    def __init__(self, session: requests.Session = None):
        """Initializes the OdaFtSagClient with a base API URL and optional session.

        Args:
            base_url (str, optional): The OData API root URL. Defaults to "https://oda.ft.dk/api".
            session (requests.Session, optional): If provided, uses this HTTP session for requests.
                Otherwise, creates a new session.
        """
        self.base_url = "https://oda.ft.dk/api"
        self.session = session or requests.Session()

    def _get(self, path: str, params: dict = None) -> dict:
        """Performs a GET request for JSON data, raising an error if the response is unsuccessful.

        Args:
            path (str): The path (relative to base_url) for the request, e.g. "Sag(12345)".
            params (dict, optional): Query parameters to include in the request. Defaults to None.

        Returns:
            dict: The JSON-decoded response body as a Python dictionary.

        Raises:
            HTTPError: If the response contains an HTTP error status code.
        """
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def _fetch_all_pages(self, initial_url: str) -> list:
        """Fetches all pages of a paginated OData response, following 'odata.nextLink' if present.

        Args:
            initial_url (str): The fully-formed URL (including query parameters) for the first page.

        Returns:
            list: A combined list of all items from each page in the result set.
        """
        all_items = []
        next_url = initial_url

        while next_url:
            if not next_url.startswith("http"):
                # If the next link is relative, construct absolute:
                next_url = urllib.parse.urljoin(self.base_url, next_url)

            resp = self.session.get(next_url)
            resp.raise_for_status()
            data = resp.json()

            items = data.get('value')
            if items is None:
                items = data.get('d', {}).get('results', [])

            all_items.extend(items)

            next_link = data.get('odata.nextLink')
            if next_link:
                next_url = next_link
            else:
                next_url = None

        return all_items
    

    def fetch_complete_sag(self, sag_id: int):
        ...

    def fetch_sag_id_from_nummer(self, sag_nummer: int):
        ...

    def fetch_periode(self, periode_id: int):
        ...

    