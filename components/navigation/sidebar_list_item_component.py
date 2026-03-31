from typing import Pattern
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text
import allure


class SidebarListItemComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier
        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', name=f"{identifier} sidebar icon")
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', name=f'{identifier} sidebar title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', name=f"{identifier} sidebar button")

    @allure.step('Check visible "{title}" sidebar list item')
    def check_visible(self, title: str):
        self.icon.check_visible(identifier=self.identifier)

        self.title.check_visible(identifier=self.identifier)
        self.title.check_have_text(title, identifier=self.identifier)

        self.button.check_visible(identifier=self.identifier)

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)
