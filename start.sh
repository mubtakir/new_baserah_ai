#!/bin/bash

# 🌟 نظام بصيرة الثوري - مُشغل سريع
# 🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

echo "======================================================================="
echo "🌟 نظام بصيرة الثوري - مُشغل سريع"
echo "🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله"
echo "📅 التاريخ: $(date '+%Y-%m-%d %H:%M:%S')"
echo "======================================================================="

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 غير مثبت. يرجى تثبيت Python 3.8 أو أحدث"
    exit 1
fi

echo "✅ تم العثور على Python3: $(python3 --version)"

# التحقق من وجود pip
if ! command -v pip &> /dev/null && ! command -v pip3 &> /dev/null; then
    echo "❌ pip غير مثبت. يرجى تثبيت pip"
    exit 1
fi

# تثبيت المتطلبات إذا لم تكن مثبتة
echo "🔍 فحص المتطلبات..."
if [ -f "requirements.txt" ]; then
    echo "📦 تثبيت المتطلبات..."
    pip install -r requirements.txt --quiet
    if [ $? -eq 0 ]; then
        echo "✅ تم تثبيت المتطلبات بنجاح"
    else
        echo "⚠️ تحذير: قد تكون هناك مشاكل في تثبيت بعض المتطلبات"
    fi
else
    echo "⚠️ ملف requirements.txt غير موجود"
fi

echo ""
echo "🚀 تشغيل نظام بصيرة الثوري..."
echo ""

# تشغيل النظام
python3 run_basera.py

echo ""
echo "👋 شكراً لاستخدام نظام بصيرة الثوري!"
echo "🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله"
