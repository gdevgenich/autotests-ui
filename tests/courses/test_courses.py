from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Остальной код без изменений
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    create_course_page.create_course_form.check_visible(title="", description_text="", estimated_time="", max_score="0",
                                                        min_score='0')
    create_course_page.create_course_exercises_toolbar.check_visible()
    create_course_page.exercises_empty_view.check_visible(title="There is no exercises",
                                               description='Click on "Create exercise" button to create new exercise')

    # Fill course fields
    create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(title="Playwrite", estimated_time="2 weeks", description_text="Playwrite",
                                               max_score="100", min_score="10")
    create_course_page.create_course_toolbar.click_create_course_button()

    # Check values on course list page
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(index=0, title="Playwrite", estimated_time="2 weeks",
                                                max_score="100", min_score="10")


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.empty_view.check_visible(title="There is no results",
                                               description="Results from the load test pipeline will be displayed here")
