import pandas as pd
from langchain.agents import load_tools, initialize_agent, Tool
from langchain.utilities import GoogleSerperAPIWrapper
import ast


class web_search_agent:
    def __init__(self, model, tools=None, verbose=False):
        # Google search tool
        if tools is None:
            google_search = GoogleSerperAPIWrapper()
            tools = [
                Tool(
                    name="Intermediate Answer",
                    func=google_search.run,
                    description="useful for when you need to ask with search"
                )
            ]
        
        # Initialize agent
        self.agent = initialize_agent(tools, model, agent="zero-shot-react-description", verbose=verbose)
        
    def assets(self, assets_array, prompt=None, max_retries=2):
        if prompt is None:
            self.search_asset_prompt = """
            Search for information on the financial instrument %s with id %s. Return the information in the following format using the specified rules for each field:
            {
            'Asset class': 'Value should be selected from the list [Equity, Bond, Money Market, Real Estate, Private Debt, Private equity, Cryptoassets, Alternatives, Other']. If unsure or information is unavailable, return NA.,
            'Currency': 'Value must be the currency using 3 characters convention, e.g. USD, EUR',
            'Country': 'Value must be the country following th 2 characters ISO code convention, e.g., US, FR',
            'Market': 'Value must be selected from the list [emerging markets, developed markets, global, other]',
            'Rating': 'Value must be selected from the list [government bond, high yield, investment grade, other]',
            'Type': 'Value must be selected from the list [stock, bond , derivative, fund , other]'
            }
            """
        else:
            self.search_asset_prompt = prompt

        items = []
        for item in assets_array:
            print(f"Searching {item['id']} with id {item['isin']}")
            retries = 0
            success = False
            while retries < max_retries and not success:
                try:
                    response = self.agent.run(self.search_asset_prompt % (item['id'], item['isin']))
                    parsed_response = ast.literal_eval(response)
                    item = {
                        **{'Isin': item['isin'], 'Name': item['id']},
                        **parsed_response
                    }
                    success = True  # Mark as successful
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        item = {
                            'Isin': item['isin'],
                            'Name': item['id'],
                            'Asset class': '',
                            'Currency': '',
                            'Country': '',
                            'Market': '',
                            'Rating': '',
                            'Type': ''
                        }
                        print(f"Failed to identify instrument after {retries} retries: {str(e)}")
                    else:
                        print(f"Retrying ({retries}/{max_retries}) due to error: {str(e)}")

            items.append(item)
        
        return pd.DataFrame(items)