import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.parametrize("resize_x, resize_y", [(100, 50), (-50, -30)])
def test_resize_behavior(resize_x, resize_y):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # Example: jQuery UI resizable demo
        page.goto("https://jqueryui.com/resizable/#fillspace")

        # Switch into iframe where the widget lives
        frame = page.frame_locator("iframe.demo-frame")

        # Locate resizer container and handle
        resizer = frame.locator("#resizable")
        handle = frame.locator(".ui-resizable-se")

        # Record initial bounding box
        box_before = resizer.bounding_box()

        # Perform resize (drag the handle)
        handle.drag_to(
            handle,
            target_position={"x": handle.bounding_box()["width"] + resize_x,
                             "y": handle.bounding_box()["height"] + resize_y}
        )

        # Record bounding box after resize
        box_after = resizer.bounding_box()

        # Assertions: width/height changed according to drag
        assert box_after["width"] != box_before["width"]
        assert box_after["height"] != box_before["height"]

        browser.close()
