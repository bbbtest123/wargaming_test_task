import pytest

from test.pages import wiki_programming_languages


@pytest.mark.usefixtures("before_and_after")
class TestWikiSelenium:
    @pytest.mark.parametrize("threshold",
                             [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
    def test_wiki_programming_languages(self, threshold):
        errors = []

        for website in wiki_programming_languages.get_websites(driver=pytest.driver):
            if website.popularity < threshold:
                errors.append(f"{str(website)} has {website.popularity} unique visitors per month. "
                              f"(Expected more than {int(threshold)})")

        assert not errors, "\n".join(errors)
