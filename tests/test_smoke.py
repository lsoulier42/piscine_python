"""Tests partiels : ils échouent avant l'implémentation des exercices."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(mod, ex, name):
    path = ROOT / mod / ex / name
    spec = importlib.util.spec_from_file_location(f"student_{mod}_{ex}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class TestPy00(unittest.TestCase):
    def test_slug(self):
        fn = load("py00", "ex02", "slug.py").slugify
        self.assertEqual(fn("  Bonjour   PHP Python  "), "bonjour-php-python")
        self.assertEqual(fn(""), "")
    def test_fizzbuzz(self):
        fn = load("py00", "ex03", "fizz.py").fizzbuzz
        self.assertEqual(fn(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(fn(15)[-1], "FizzBuzz")
        self.assertEqual(fn(0), [])
    def test_invoice(self):
        fn = load("py00", "ex04", "invoice.py").total_with_tax
        self.assertEqual(fn([1000, 250], 20), 1500)
        self.assertEqual(fn([], 20), 0)
        with self.assertRaises(ValueError):
            fn([-1], 20)

class TestPy01(unittest.TestCase):
    def test_active(self):
        fn = load("py01", "ex00", "filter_users.py").active_names
        self.assertEqual(fn([{"name": "Ada", "active": True}, {"name": "Bob", "active": False}]), ["Ada"])
    def test_counts(self):
        fn = load("py01", "ex01", "word_count.py").word_counts
        self.assertEqual(fn("Go go Python"), {"go": 2, "python": 1})
    def test_stock(self):
        fn = load("py01", "ex02", "inventory.py").merge_stock
        a = {"A": 2}
        self.assertEqual(fn(a, {"A": 3, "B": 1}), {"A": 5, "B": 1})
        self.assertEqual(a, {"A": 2})
    def test_unique(self):
        fn = load("py01", "ex03", "unique.py").unique_in_order
        self.assertEqual(fn(["a", "b", "a", "c"]), ["a", "b", "c"])
    def test_cart(self):
        fn = load("py01", "ex04", "cart.py").summarize_cart
        self.assertEqual(fn([{"sku": "A", "quantity": 2, "unit_price": 300}, {"sku": "A", "quantity": 1, "unit_price": 300}]), {"total_cents": 900, "quantities": {"A": 3}})

class TestPy02(unittest.TestCase):
    def test_parse(self):
        fn = load("py02", "ex00", "parse_int.py").parse_positive_int
        self.assertEqual(fn(" +42 "), 42)
        with self.assertRaises(ValueError):
            fn("-2")
    def test_options(self):
        fn = load("py02", "ex01", "options.py").make_url
        self.assertEqual(fn("/search", q="chat noir", page="2"), "/search?q=chat+noir&page=2")
    def test_pages(self):
        fn = load("py02", "ex02", "paginate.py").paginate
        self.assertEqual(fn([0, 1, 2, 3, 4], 2, 2), [2, 3])
        self.assertEqual(fn([], 1, 10), [])
        with self.assertRaises(ValueError):
            fn([], 0, 10)
    def test_validation(self):
        fn = load("py02", "ex03", "validation.py").validate_user
        self.assertEqual(fn({"email": " ADA@EXAMPLE.COM ", "age": 32, "extra": 1}), {"email": "ada@example.com", "age": 32})
        with self.assertRaises(ValueError):
            fn({"email": "a@b", "age": True})

class TestPy05(unittest.TestCase):
    def test_chunks(self):
        fn = load("py05", "ex01", "chunks.py").chunks
        self.assertEqual(list(fn([1, 2, 3, 4, 5], 2)), [[1, 2], [3, 4], [5]])

class TestPy06(unittest.TestCase):
    def test_total_order(self):
        fn = load("py06", "ex00", "typed_orders.py").total_order
        self.assertEqual(fn([("A", 2, 150), ("B", 1, 20)]), 320)
    def test_route(self):
        fn = load("py06", "ex01", "router.py").route
        self.assertEqual(fn(" STATUS "), "OK")
        self.assertEqual(fn("other"), "Unknown command")

if __name__ == "__main__":
    unittest.main()
