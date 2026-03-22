from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.button import Button
from elements.text import Text
from elements.file_input import FileInput

class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)
        self.identifier = identifier
        self.preview_empty_view = EmptyViewComponent(page, identifier)
        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image',
                                   name="upload form preview image")
        self.image_upload_info_icon = Icon(page,f'{identifier}-image-upload-widget-info-icon',
                                           "upload form icon")
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text',
                                            name="upload form title text")
        self.image_upload_info_description = Text(page,f'{identifier}-image-upload-widget-info-description-text',
                                                  name="upload form description text")

        self.upload_button = Button(page, f'{identifier}-image-upload-widget-upload-button',
                                    "upload form upload button")
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button',
                                    name="upload form remove button")
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', name="upload form input field")

    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible(identifier=self.identifier)

        self.image_upload_info_title.check_visible(identifier=self.identifier)
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file',
                                                     identifier=self.identifier)

        self.image_upload_info_description.check_visible(identifier=self.identifier)
        self.image_upload_info_description.check_have_text('Recommended file size 540X300',
                                                           identifier=self.identifier)

        self.upload_button.check_visible(identifier=self.identifier)

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible(identifier=self.identifier)
            self.preview_image.check_visible(identifier=self.identifier)

        if not is_image_uploaded:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)
