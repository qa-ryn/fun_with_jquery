from playwright.sync_api import Page
from pages.accordion_page import AccordionPage

def test_default_functionality(page: Page):
    run =  AccordionPage(page)
    run.load_page("https://jqueryui.com/accordion/#default")
    run.default_functionality()
    
def test_collapse_content(page: Page):
    run =  AccordionPage(page)
    run.load_page("https://jqueryui.com/accordion/#collapsible")
    run.collapse_content()