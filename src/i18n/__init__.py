"""Internationalization (i18n) modules for bilingual support."""

from src.i18n.language_detector import LanguageDetector
from src.i18n.font_selector import FontSelector
from src.i18n.layout_adjuster import LayoutAdjuster

__all__ = ['LanguageDetector', 'FontSelector', 'LayoutAdjuster']
