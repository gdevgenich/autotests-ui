from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text
import allure


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier
        self.icon = Icon(page, f'{identifier}-empty-view-icon', name="empty view icon")
        self.title = Text(page, f'{identifier}-empty-view-title-text', name="empty view title")
        self.description = Text(page,f'{identifier}-empty-view-description-text', name="empty view description")

    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str):
        # Проверяем видимость иконки
        self.icon.check_visible(identifier=self.identifier)

        # Проверяем видимость заголовка и его текст
        self.title.check_visible(identifier=self.identifier)
        self.title.check_have_text(title, identifier=self.identifier)

        # Проверяем видимость описания и его текст
        self.description.check_visible(identifier=self.identifier)
        self.description.check_have_text(description, identifier=self.identifier)
