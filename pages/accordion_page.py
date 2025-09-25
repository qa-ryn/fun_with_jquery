from playwright.sync_api import Page, expect

class AccordionPage:
    sections = [
        ("Section 1", "#ui-id-2", ["Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam."]),
        ("Section 2", "#ui-id-4", ["Sed non urna. Donec et ante. Phasellus eu ligula."]),
        ("Section 3", "#ui-id-6", ["Nam enim risus, molestie et, porta ac, aliquam ac, risus."]),
        ("Section 4", "#ui-id-8", ["Cras dictum. Pellentesque habitant morbi tristique senectus et" , "Suspendisse eu nisl. Nullam ut libero. Integer dignissim consequat "
        ]),
    ]
    
    def __init__(self, page: Page):
        self.page = page
        
    def functionality(self, sections):
        print("\n")
        
        self.page.get_by_role("link", name="Accordion").click()
        iframe = self.page.locator("iframe").content_frame
        
        #Iterate for every Section
        for section_name, section_locator, expected_text in sections:
            print(f"{section_name} start checking...")
            iframe.get_by_role("tab", name=section_name).click()
            self.page.wait_for_timeout(1000)
            panel = iframe.locator(section_locator)
            
            #Validate if the Section Panel opened correctly
            expect(panel).to_have_attribute("aria-hidden", "false")
            
            #Isolate paragrah text in each Section
            section_text = panel.locator("p")
            section_text_all = section_text.all_inner_texts()
            
            #print(section_text.all_inner_texts())
            print("=== Paragraphs ===")
            for i, t in enumerate(section_text_all, start=1):
                print(f"- {i}: {t}")
            print("")
            expect(section_text).to_contain_text(expected_text)
            
            #Isolate list item inside Section 3 
            if section_name == "Section 3":
                items = iframe.locator("li")
                count = items.count()
                
                for i in range(count):
                    text = items.nth(i).inner_text()
                    print(text)
                print("\n")
            