from unittest import TestCase

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


class IndexTests(TestCase):
    """Tests for the index route."""

    def test_index(self):
        """Test that the index page shows "Hello, World!" """
        res = app.test_client().get("/")
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        expected_page_text = "Hello, World!"
        self.assertEqual(expected_page_text, result_page_text)


#######################
# Favorite Color Tests
#######################


class ColorTests(TestCase):
    """Tests for the Color route."""

    def test_color_results_blue(self):
        result = app.test_client().get("/color_results?color=blue")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "Wow, blue is my favorite color, too!"
        self.assertEqual(expected_page_text, result_page_text)

    def test_color_results_light_green(self):
        result = app.test_client().get("/color_results?color=light+green")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "Wow, light green is my favorite color, too!"
        self.assertEqual(expected_page_text, result_page_text)

    def test_color_results_empty(self):
        result = app.test_client().get("/color_results?color=")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You didn't specify a color!"
        self.assertEqual(expected_page_text, result_page_text)


#######################
# Froyo Tests
#######################


class FroyoTests(TestCase):
    def test_froyo_results_scenario1(self):
        result = app.test_client().get("/froyo_results?flavor=vanilla&toppings=banana")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You ordered vanilla flavored Fro-Yo with toppings banana!"
        self.assertEqual(expected_page_text, result_page_text)

    def test_froyo_results_scenario2(self):
        result = app.test_client().get(
            "/froyo_results?flavor=vanilla&toppings=banana+%26+peanuts"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = (
            "You ordered vanilla flavored Fro-Yo with toppings banana & peanuts!"
        )
        self.assertEqual(expected_page_text, result_page_text)

    def test_froyo_results_edgecase1(self):
        result = app.test_client().get("/froyo_results?flavor=chocolate&toppings=")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You ordered chocolate flavored Fro-Yo with toppings !"
        self.assertEqual(expected_page_text, result_page_text)

    def test_froyo_results_edgecase2(self):
        result = app.test_client().get("/froyo_results?flavor=&toppings=gummy+bears")

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You ordered  flavored Fro-Yo with toppings gummy bears!"
        self.assertEqual(expected_page_text, result_page_text)


#######################
# Reverse Message Tests
#######################


class MessageTests(TestCase):
    def test_message_results_helloworld(self):
        form_data = {"message": "Hello World"}
        res = app.test_client().post("/message_results", data=form_data)
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        self.assertIn("dlroW olleH", result_page_text)

    def test_message_results_scenario2(self):
        form_data = {"message": "RacecaR"}
        res = app.test_client().post("/message_results", data=form_data)
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        self.assertIn("RacecaR", result_page_text)

    def test_message_results_edgecase1(self):
        form_data = {"message": ""}
        res = app.test_client().post("/message_results", data=form_data)
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        expected_page_text = "Here's your reversed message: "
        self.assertEqual(expected_page_text, result_page_text)


#######################
# Calculator Tests
#######################


class CalculatorTests(TestCase):
    def test_calculator_results_scenario1(self):
        result = app.test_client().get(
            "/calculator_results?operand1=1&operation=add&operand2=1"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You chose to add 1 and 1. Your result is: 2"
        self.assertEqual(expected_page_text, result_page_text)

    def test_calculator_results_scenario2(self):
        result = app.test_client().get(
            "/calculator_results?operand1=1&operation=subtract&operand2=2"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You chose to subtract 1 and 2. Your result is: -1"
        self.assertEqual(expected_page_text, result_page_text)

    def test_calculator_results_scenario3(self):
        result = app.test_client().get(
            "/calculator_results?operand1=1&operation=multiply&operand2=-1"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You chose to multiply 1 and -1. Your result is: -1"
        self.assertEqual(expected_page_text, result_page_text)

    def test_calculator_results_scenario4(self):
        result = app.test_client().get(
            "/calculator_results?operand1=1&operation=divide&operand2=-2"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You chose to divide 1 and -2. Your result is: -0.5"
        self.assertEqual(expected_page_text, result_page_text)

    def test_calculator_results_edgecase1(self):
        result = app.test_client().get(
            "/calculator_results?operand1=1&operation=divide&operand2=0"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "Cannot divide by 0!"
        self.assertEqual(expected_page_text, result_page_text)

    def test_calculator_results_edgecase2(self):
        result = app.test_client().get(
            "/calculator_results?operand1=0&operation=divide&operand2=-1"
        )

        self.assertEqual(result.status_code, 200)

        result_page_text = result.get_data(as_text=True)
        expected_page_text = "You chose to divide 0 and -1. Your result is: -0.0"
        self.assertEqual(expected_page_text, result_page_text)
