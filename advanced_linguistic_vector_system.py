#!/usr/bin/env python3
"""
نظام المتجهات اللغوية المتقدم - Advanced Linguistic Vector System
نظام بصيرة الثوري

🔤 تحويل الكلمات والنصوص إلى متجهات رياضية
🧬 يعتمد على النظريات الثلاث الثورية
⚡ معالجة متقدمة للغة العربية
🎯 دعم التحليل الدلالي والسياقي

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import numpy as np
import re
import json
import math
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import uuid

# استيراد المكونات الأساسية
from core_interfaces import BaseComponent
from revolutionary_mother_equation import RevolutionaryMotherEquation

class VectorType(Enum):
    """أنواع المتجهات اللغوية"""
    WORD_VECTOR = "word_vector"
    SENTENCE_VECTOR = "sentence_vector"
    SEMANTIC_VECTOR = "semantic_vector"
    CONTEXTUAL_VECTOR = "contextual_vector"
    MORPHOLOGICAL_VECTOR = "morphological_vector"

class LanguageType(Enum):
    """أنواع اللغات المدعومة"""
    ARABIC = "arabic"
    ENGLISH = "english"
    MIXED = "mixed"

@dataclass
class LinguisticVector:
    """متجه لغوي"""
    word: str
    vector: np.ndarray
    vector_type: VectorType
    language: LanguageType
    semantic_weight: float = 1.0
    contextual_weight: float = 1.0
    morphological_features: Dict[str, Any] = field(default_factory=dict)
    creation_time: datetime = field(default_factory=datetime.now)
    vector_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class SemanticRelationship:
    """علاقة دلالية بين الكلمات"""
    word1: str
    word2: str
    relationship_type: str  # synonym, antonym, related, etc.
    strength: float  # 0-1
    context: Optional[str] = None

class ArabicMorphologyAnalyzer:
    """محلل الصرف العربي"""
    
    def __init__(self):
        # قواعد الصرف العربية الأساسية
        self.prefixes = ['ال', 'و', 'ف', 'ب', 'ك', 'ل', 'من', 'إلى', 'على', 'في']
        self.suffixes = ['ة', 'ان', 'ين', 'ون', 'ات', 'ها', 'هم', 'هن', 'كم', 'كن']
        self.patterns = {
            'فعل': ['فعل', 'فعال', 'فاعل', 'مفعول', 'فعيل'],
            'اسم': ['فعال', 'فعيل', 'فاعل', 'مفعل'],
            'صفة': ['فعيل', 'فعال', 'أفعل', 'فاعل']
        }
    
    def analyze_word(self, word: str) -> Dict[str, Any]:
        """تحليل كلمة عربية"""
        analysis = {
            'original_word': word,
            'root': self._extract_root(word),
            'prefix': self._extract_prefix(word),
            'suffix': self._extract_suffix(word),
            'pattern': self._identify_pattern(word),
            'word_type': self._classify_word_type(word),
            'morphological_features': self._extract_features(word)
        }
        return analysis
    
    def _extract_root(self, word: str) -> str:
        """استخراج الجذر"""
        # إزالة البادئات واللواحق
        clean_word = word
        for prefix in self.prefixes:
            if clean_word.startswith(prefix):
                clean_word = clean_word[len(prefix):]
                break
        
        for suffix in self.suffixes:
            if clean_word.endswith(suffix):
                clean_word = clean_word[:-len(suffix)]
                break
        
        # استخراج الجذر الثلاثي أو الرباعي
        if len(clean_word) >= 3:
            return clean_word[:3]  # تبسيط للجذر الثلاثي
        return clean_word
    
    def _extract_prefix(self, word: str) -> Optional[str]:
        """استخراج البادئة"""
        for prefix in self.prefixes:
            if word.startswith(prefix):
                return prefix
        return None
    
    def _extract_suffix(self, word: str) -> Optional[str]:
        """استخراج اللاحقة"""
        for suffix in self.suffixes:
            if word.endswith(suffix):
                return suffix
        return None
    
    def _identify_pattern(self, word: str) -> str:
        """تحديد الوزن الصرفي"""
        # تبسيط لتحديد الوزن
        if len(word) == 3:
            return "فعل"
        elif len(word) == 4:
            return "فعال"
        elif len(word) == 5:
            return "فاعل"
        else:
            return "مركب"
    
    def _classify_word_type(self, word: str) -> str:
        """تصنيف نوع الكلمة"""
        # تصنيف مبسط
        if word.endswith('ة'):
            return "اسم_مؤنث"
        elif word.startswith('ال'):
            return "اسم_معرف"
        else:
            return "اسم_نكرة"
    
    def _extract_features(self, word: str) -> Dict[str, Any]:
        """استخراج الخصائص الصرفية"""
        return {
            'length': len(word),
            'has_prefix': self._extract_prefix(word) is not None,
            'has_suffix': self._extract_suffix(word) is not None,
            'vowel_count': len([c for c in word if c in 'اةيوأإآ']),
            'consonant_count': len([c for c in word if c not in 'اةيوأإآ'])
        }

class AdvancedLinguisticVectorSystem(BaseComponent):
    """نظام المتجهات اللغوية المتقدم"""
    
    def __init__(self, name: str = "AdvancedLinguisticVectorSystem"):
        super().__init__(name)
        
        # المكونات الأساسية
        self.morphology_analyzer = ArabicMorphologyAnalyzer()
        self.word_vectors: Dict[str, LinguisticVector] = {}
        self.semantic_relationships: List[SemanticRelationship] = []
        self.vector_dimension = 100  # أبعاد المتجه
        
        # المعادلة الأم للحسابات
        self.mother_equation = None
        self._initialize_mother_equation()
        
        # قواميس دلالية أساسية
        self.semantic_categories = self._initialize_semantic_categories()
        self.contextual_weights = self._initialize_contextual_weights()
        
        # إحصائيات النظام
        self.stats = {
            'total_vectors': 0,
            'arabic_vectors': 0,
            'english_vectors': 0,
            'semantic_relationships': 0,
            'processing_time': 0.0
        }
    
    def initialize(self) -> bool:
        """تهيئة النظام"""
        try:
            print(f"🔤⚡ تم إنشاء نظام المتجهات اللغوية المتقدم: {self.name}")
            print(f"   📊 أبعاد المتجه: {self.vector_dimension}")
            print(f"   🧬 محلل الصرف العربي: نشط")
            print(f"   📚 الفئات الدلالية: {len(self.semantic_categories)}")
            
            self.is_initialized = True
            return True
        except Exception as e:
            print(f"❌ فشل تهيئة نظام المتجهات اللغوية: {e}")
            return False
    
    def _initialize_mother_equation(self):
        """تهيئة المعادلة الأم"""
        try:
            # إنشاء معادلة أم مخصصة للمتجهات اللغوية
            class LinguisticMotherEquation(RevolutionaryMotherEquation):
                def __init__(self, name):
                    super().__init__(name)
                
                def process_input(self, input_data: Any) -> Any:
                    return input_data
                
                def generate_output(self, processed_data: Any) -> Any:
                    return processed_data
            
            self.mother_equation = LinguisticMotherEquation("LinguisticVectorEquation")
        except Exception as e:
            print(f"⚠️ تحذير: فشل إنشاء المعادلة الأم للمتجهات: {e}")
    
    def _initialize_semantic_categories(self) -> Dict[str, List[str]]:
        """تهيئة الفئات الدلالية"""
        return {
            'إيجابي': ['خير', 'نور', 'حب', 'سلام', 'فرح', 'أمل', 'نجاح', 'جمال'],
            'سلبي': ['شر', 'ظلام', 'كره', 'حرب', 'حزن', 'يأس', 'فشل', 'قبح'],
            'طبيعة': ['شمس', 'قمر', 'نجم', 'بحر', 'جبل', 'شجر', 'زهر', 'ماء'],
            'إنسان': ['رجل', 'امرأة', 'طفل', 'أب', 'أم', 'أخ', 'أخت', 'صديق'],
            'علم': ['كتاب', 'قلم', 'مدرسة', 'معلم', 'طالب', 'درس', 'امتحان', 'شهادة'],
            'دين': ['الله', 'رسول', 'قرآن', 'صلاة', 'صوم', 'حج', 'زكاة', 'إيمان'],
            'زمن': ['يوم', 'ليل', 'صباح', 'مساء', 'أمس', 'اليوم', 'غد', 'سنة'],
            'مكان': ['بيت', 'مدينة', 'قرية', 'شارع', 'حديقة', 'مسجد', 'مدرسة', 'مستشفى']
        }
    
    def _initialize_contextual_weights(self) -> Dict[str, float]:
        """تهيئة أوزان السياق"""
        return {
            'قرآني': 1.0,
            'ديني': 0.9,
            'أدبي': 0.8,
            'علمي': 0.7,
            'يومي': 0.6,
            'عامي': 0.5
        }
    
    def process(self, input_data: Any) -> Any:
        """معالجة البيانات اللغوية"""
        if isinstance(input_data, str):
            return self.create_word_vector(input_data)
        elif isinstance(input_data, list):
            return [self.create_word_vector(word) for word in input_data]
        else:
            return None
    
    def create_word_vector(self, word: str, context: str = "عام") -> LinguisticVector:
        """إنشاء متجه لكلمة"""
        start_time = datetime.now()
        
        # تحديد نوع اللغة
        language = self._detect_language(word)
        
        # تحليل صرفي للعربية
        morphological_features = {}
        if language == LanguageType.ARABIC:
            morphological_features = self.morphology_analyzer.analyze_word(word)
        
        # إنشاء المتجه الأساسي
        base_vector = self._generate_base_vector(word, language)
        
        # إضافة الخصائص الدلالية
        semantic_vector = self._add_semantic_features(base_vector, word)
        
        # إضافة الخصائص السياقية
        contextual_vector = self._add_contextual_features(semantic_vector, word, context)
        
        # إضافة الخصائص الصرفية
        final_vector = self._add_morphological_features(contextual_vector, morphological_features)
        
        # إنشاء المتجه اللغوي
        linguistic_vector = LinguisticVector(
            word=word,
            vector=final_vector,
            vector_type=VectorType.WORD_VECTOR,
            language=language,
            semantic_weight=self._calculate_semantic_weight(word),
            contextual_weight=self.contextual_weights.get(context, 0.5),
            morphological_features=morphological_features
        )
        
        # حفظ المتجه
        self.word_vectors[word] = linguistic_vector
        
        # تحديث الإحصائيات
        self._update_stats(language, start_time)
        
        return linguistic_vector
    
    def _detect_language(self, word: str) -> LanguageType:
        """كشف نوع اللغة"""
        arabic_chars = set('ابتثجحخدذرزسشصضطظعغفقكلمنهوياةأإآ')
        english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        word_chars = set(word)
        
        if word_chars & arabic_chars:
            if word_chars & english_chars:
                return LanguageType.MIXED
            else:
                return LanguageType.ARABIC
        elif word_chars & english_chars:
            return LanguageType.ENGLISH
        else:
            return LanguageType.MIXED
    
    def _generate_base_vector(self, word: str, language: LanguageType) -> np.ndarray:
        """إنشاء المتجه الأساسي"""
        # استخدام المعادلة الأم لإنشاء المتجه
        vector = np.zeros(self.vector_dimension)
        
        # تحويل الأحرف إلى قيم رقمية
        for i, char in enumerate(word[:self.vector_dimension]):
            char_value = ord(char) / 1000.0
            
            # تطبيق النظريات الثلاث الثورية
            if self.mother_equation:
                # نظرية ثنائية الصفر
                zero_duality = math.sin(char_value * math.pi) * math.cos(char_value * math.pi)
                
                # نظرية تعامد الأضداد
                perpendicular = math.sin(char_value) * math.cos(char_value + math.pi/2)
                
                # نظرية الفتائل
                filament = math.exp(-char_value) * math.sin(char_value * 2 * math.pi)
                
                # دمج النظريات
                vector[i % self.vector_dimension] = (zero_duality + perpendicular + filament) / 3
            else:
                vector[i % self.vector_dimension] = char_value
        
        # تطبيع المتجه
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        
        return vector
    
    def _add_semantic_features(self, base_vector: np.ndarray, word: str) -> np.ndarray:
        """إضافة الخصائص الدلالية"""
        semantic_vector = base_vector.copy()
        
        # البحث في الفئات الدلالية
        for category, words in self.semantic_categories.items():
            if word in words:
                # إضافة وزن دلالي للفئة
                category_weight = hash(category) % 100 / 100.0
                semantic_vector += category_weight * 0.1
        
        return semantic_vector
    
    def _add_contextual_features(self, semantic_vector: np.ndarray, word: str, context: str) -> np.ndarray:
        """إضافة الخصائص السياقية"""
        contextual_vector = semantic_vector.copy()
        
        # تطبيق وزن السياق
        context_weight = self.contextual_weights.get(context, 0.5)
        contextual_vector *= context_weight
        
        return contextual_vector
    
    def _add_morphological_features(self, contextual_vector: np.ndarray, morphological_features: Dict[str, Any]) -> np.ndarray:
        """إضافة الخصائص الصرفية"""
        final_vector = contextual_vector.copy()
        
        if morphological_features:
            # إضافة خصائص الجذر
            if 'root' in morphological_features:
                root = morphological_features['root']
                root_weight = len(root) / 10.0
                final_vector += root_weight * 0.05
            
            # إضافة خصائص الوزن
            if 'pattern' in morphological_features:
                pattern = morphological_features['pattern']
                pattern_weight = hash(pattern) % 100 / 100.0
                final_vector += pattern_weight * 0.03
        
        return final_vector
    
    def _calculate_semantic_weight(self, word: str) -> float:
        """حساب الوزن الدلالي"""
        weight = 0.5  # وزن افتراضي
        
        # زيادة الوزن للكلمات في الفئات الدلالية
        for category, words in self.semantic_categories.items():
            if word in words:
                if category in ['دين', 'قرآني']:
                    weight += 0.3
                elif category in ['إيجابي', 'علم']:
                    weight += 0.2
                else:
                    weight += 0.1
        
        return min(weight, 1.0)  # تحديد الحد الأقصى
    
    def _update_stats(self, language: LanguageType, start_time: datetime):
        """تحديث الإحصائيات"""
        self.stats['total_vectors'] += 1
        
        if language == LanguageType.ARABIC:
            self.stats['arabic_vectors'] += 1
        elif language == LanguageType.ENGLISH:
            self.stats['english_vectors'] += 1
        
        processing_time = (datetime.now() - start_time).total_seconds()
        self.stats['processing_time'] += processing_time

# اختبار النظام
def test_linguistic_vector_system():
    """اختبار نظام المتجهات اللغوية"""
    print("🧪 اختبار نظام المتجهات اللغوية المتقدم")
    print("=" * 50)
    
    # إنشاء النظام
    system = AdvancedLinguisticVectorSystem()
    system.initialize()
    
    # كلمات تجريبية
    test_words = ['الله', 'رسول', 'قرآن', 'نور', 'هداية', 'cat', 'love', 'peace']
    
    print(f"\n🔤 اختبار إنشاء المتجهات:")
    for word in test_words:
        vector = system.create_word_vector(word, 'ديني')
        print(f"   📊 {word}: متجه {vector.vector.shape} | لغة: {vector.language.value}")
        print(f"      🎯 وزن دلالي: {vector.semantic_weight:.3f}")
        print(f"      🧬 وزن سياقي: {vector.contextual_weight:.3f}")
    
    # عرض الإحصائيات
    print(f"\n📈 إحصائيات النظام:")
    print(f"   📊 إجمالي المتجهات: {system.stats['total_vectors']}")
    print(f"   🔤 متجهات عربية: {system.stats['arabic_vectors']}")
    print(f"   🔤 متجهات إنجليزية: {system.stats['english_vectors']}")
    print(f"   ⏱️ وقت المعالجة: {system.stats['processing_time']:.3f}s")
    
    print(f"\n✅ انتهى اختبار نظام المتجهات اللغوية!")
    return system

if __name__ == "__main__":
    test_linguistic_vector_system()
