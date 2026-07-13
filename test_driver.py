import unittest
from unittest.mock import patch, MagicMock, call

# Import the function under test
from driver import driver


class TestDriverFunction(unittest.TestCase):

    @patch("driver.driver")
    @patch("driver.webdriver.Chrome")
    def test_driver_navigates_pages_and_collects_books(self, mock_chrome_cls, mock_scrape):
        # Fake driver instance
        mock_driver = MagicMock()
        mock_chrome_cls.return_value = mock_driver

        # Simulate URLs for each page as the loop progresses
        # The code does:
        #   while True:
        #       books.append(scrape(d.current_url))
        #       if d.current_url == "page-50": break
        #
        # So we need current_url to change each iteration.
        urls = [
            "https://books.toscrape.com/catalogue/page-1.html",
            "https://books.toscrape.com/catalogue/page-2.html",
            "https://books.toscrape.com/catalogue/page-50.html",
        ]

        # Use side_effect so each access to .current_url returns the next URL
        type(mock_driver).current_url = unittest.mock.PropertyMock(side_effect=urls)

        # Mock find_element for the "next" button chain
        mock_next_li = MagicMock()
        mock_next_link = MagicMock()
        mock_driver.find_element.return_value = mock_next_li
        mock_next_li.find_element.return_value = mock_next_link

        # Mock scrape results for each page
        mock_scrape.side_effect = [
            ["book1_page1", "book2_page1"],
            ["book1_page2"],
            ["book1_page50", "book2_page50"],
        ]

        start_url = "https://books.toscrape.com/catalogue/page-1.html"

        # Act
        result = driver(start_url)

        # Assert: scrape called once per page with the current_url
        expected_scrape_calls = [call(urls[0]), call(urls[1]), call(urls[2])]
        self.assertEqual(mock_scrape.call_args_list, expected_scrape_calls)

        # Result is list of lists from side_effect
        self.assertEqual(
            result,
            [
                ["book1_page1", "book2_page1"],
                ["book1_page2"],
                ["book1_page50", "book2_page50"],
            ],
        )

        # "next" link clicked for all but last page
        self.assertEqual(mock_next_link.click.call_count, 2)

        # Chrome called once
        mock_chrome_cls.assert_called_once()

        # quit called when finished
        mock_driver.quit.assert_called_once()

    @patch("your_module_name.scrape")
    @patch("your_module_name.webdriver.Chrome")
    def test_driver_stops_immediately_if_starting_at_page_50(self, mock_chrome_cls, mock_scrape):
        mock_driver = MagicMock()
        mock_chrome_cls.return_value = mock_driver

        # If we start on page-50, while-loop should run once then break
        url_50 = "https://books.toscrape.com/catalogue/page-50.html"
        type(mock_driver).current_url = unittest.mock.PropertyMock(return_value=url_50)

        mock_scrape.return_value = ["final_page_books"]

        # Act
        result = driver(url_50)

        # Assert
        mock_scrape.assert_called_once_with(url_50)
        mock_driver.find_element.assert_not_called()  # no "next" lookup
        mock_driver.quit.assert_called_once()
        self.assertEqual(result, [["final_page_books"]])


if __name__ == "__main__":
    unittest.main()
