@echo off
chcp 65001 >nul

echo =======================================================================
echo 🌟 نظام بصيرة الثوري - مُشغل سريع
echo 🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
echo 📅 التاريخ: %date% %time%
echo =======================================================================

REM التحقق من وجود Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python غير مثبت. يرجى تثبيت Python 3.8 أو أحدث
    pause
    exit /b 1
)

echo ✅ تم العثور على Python
python --version

REM التحقق من وجود pip
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip غير مثبت. يرجى تثبيت pip
    pause
    exit /b 1
)

REM تثبيت المتطلبات
echo 🔍 فحص المتطلبات...
if exist requirements.txt (
    echo 📦 تثبيت المتطلبات...
    pip install -r requirements.txt --quiet
    if %errorlevel% equ 0 (
        echo ✅ تم تثبيت المتطلبات بنجاح
    ) else (
        echo ⚠️ تحذير: قد تكون هناك مشاكل في تثبيت بعض المتطلبات
    )
) else (
    echo ⚠️ ملف requirements.txt غير موجود
)

echo.
echo 🚀 تشغيل نظام بصيرة الثوري...
echo.

REM تشغيل النظام
python run_basera.py

echo.
echo 👋 شكراً لاستخدام نظام بصيرة الثوري!
echo 🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
pause
