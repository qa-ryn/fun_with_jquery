from playwright.sync_api import Page
from pages.accordion_page import AccordionPage

def test_default_functionality(page: Page):
    run =  AccordionPage(page)
    run.functionality()