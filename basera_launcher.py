#!/usr/bin/env python3
"""
نظام بصيرة الثوري المكتمل - ملف التشغيل الرئيسي
Revolutionary Basera AI System - Main Launcher

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

هذا الملف يشغل النظام المكتمل بجميع مكوناته
"""

import sys
import os
import subprocess
import time
from datetime import datetime

def print_banner():
    """طباعة شعار النظام"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🌟 نظام بصيرة الثوري 🌟                    ║
    ║                Revolutionary Basera AI System                ║
    ║                                                              ║
    ║                  المطور: باسل يحيى عبدالله                   ║
    ║              جميع الأفكار والنظريات من إبداعه                ║
    ║                                                              ║
    ║  🧬 المعادلة الأم الثورية | 🧠 النواة التفكيرية متعددة الطبقات  ║
    ║  🗄️ قواعد البيانات المتخصصة | 🎨 الوحدة الفنية المحسنة      ║
    ║                    🌐 واجهة تفاعلية متكاملة                   ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def test_system_components():
    """اختبار مكونات النظام"""
    print("\n🧪 اختبار مكونات النظام...")
    print("="*60)
    
    components = [
        ("المعادلة الأم الثورية", "revolutionary_mother_equation.py"),
        ("قواعد البيانات المتخصصة", "complete_specialized_databases.py"),
        ("النواة التفكيرية", "complete_multi_layer_thinking_core.py"),
        ("الوحدة الفنية", "enhanced_artistic_unit_fixed.py")
    ]
    
    results = {}
    
    for name, filename in components:
        print(f"\n🔍 اختبار {name}...")
        try:
            result = subprocess.run([sys.executable, filename], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"   ✅ {name} - نجح الاختبار")
                results[name] = "نجح"
            else:
                print(f"   ❌ {name} - فشل الاختبار")
                print(f"   خطأ: {result.stderr[:200]}...")
                results[name] = "فشل"
        except subprocess.TimeoutExpired:
            print(f"   ⏰ {name} - انتهت مهلة الاختبار")
            results[name] = "انتهت المهلة"
        except Exception as e:
            print(f"   ❌ {name} - خطأ: {e}")
            results[name] = "خطأ"
    
    # تقرير النتائج
    print(f"\n📊 تقرير اختبار المكونات:")
    print("-" * 40)
    for name, result in results.items():
        status_icon = "✅" if result == "نجح" else "❌"
        print(f"{status_icon} {name}: {result}")
    
    successful = sum(1 for r in results.values() if r == "نجح")
    total = len(results)
    print(f"\n📈 معدل النجاح: {successful}/{total} ({successful/total*100:.1f}%)")
    
    return successful == total

def launch_interface():
    """تشغيل الواجهة التفاعلية"""
    print("\n🌐 تشغيل الواجهة التفاعلية...")
    print("="*60)
    
    try:
        print("🚀 بدء تشغيل واجهة Gradio...")
        print("📱 ستفتح الواجهة في المتصفح تلقائياً...")
        print("🔗 أو افتح الرابط المعروض يدوياً")
        print("\n⚠️  للإيقاف: اضغط Ctrl+C")
        print("-" * 40)
        
        # تشغيل الواجهة
        subprocess.run([sys.executable, "artistic_inference_interface.py"])
        
    except KeyboardInterrupt:
        print("\n\n🛑 تم إيقاف النظام بواسطة المستخدم")
    except Exception as e:
        print(f"\n❌ خطأ في تشغيل الواجهة: {e}")

def show_system_info():
    """عرض معلومات النظام"""
    print("\n📋 معلومات النظام:")
    print("-" * 40)
    print(f"🕐 وقت التشغيل: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 إصدار Python: {sys.version.split()[0]}")
    print(f"📁 مجلد العمل: {os.getcwd()}")
    
    # فحص الملفات
    required_files = [
        "revolutionary_mother_equation.py",
        "complete_multi_layer_thinking_core.py", 
        "complete_specialized_databases.py",
        "enhanced_artistic_unit_fixed.py",
        "artistic_inference_interface.py"
    ]
    
    print(f"\n📄 الملفات المطلوبة:")
    for file in required_files:
        exists = "✅" if os.path.exists(file) else "❌"
        print(f"   {exists} {file}")

def main_menu():
    """القائمة الرئيسية"""
    while True:
        print("\n" + "="*60)
        print("🌟 نظام بصيرة الثوري - القائمة الرئيسية")
        print("="*60)
        print("1️⃣  اختبار مكونات النظام")
        print("2️⃣  تشغيل الواجهة التفاعلية")
        print("3️⃣  عرض معلومات النظام")
        print("4️⃣  تشغيل مكون محدد")
        print("0️⃣  خروج")
        print("-" * 60)
        
        choice = input("🎯 اختر رقم الخيار: ").strip()
        
        if choice == "1":
            test_system_components()
        elif choice == "2":
            launch_interface()
        elif choice == "3":
            show_system_info()
        elif choice == "4":
            run_specific_component()
        elif choice == "0":
            print("\n👋 شكراً لاستخدام نظام بصيرة الثوري!")
            print("🌟 تم تطويره بواسطة: باسل يحيى عبدالله")
            break
        else:
            print("❌ خيار غير صحيح، حاول مرة أخرى")

def run_specific_component():
    """تشغيل مكون محدد"""
    components = {
        "1": ("المعادلة الأم الثورية", "revolutionary_mother_equation.py"),
        "2": ("النواة التفكيرية", "complete_multi_layer_thinking_core.py"),
        "3": ("قواعد البيانات", "complete_specialized_databases.py"),
        "4": ("الوحدة الفنية", "enhanced_artistic_unit_fixed.py"),
        "5": ("الواجهة التفاعلية", "artistic_inference_interface.py")
    }
    
    print("\n🔧 اختيار مكون للتشغيل:")
    print("-" * 40)
    for key, (name, _) in components.items():
        print(f"{key}️⃣  {name}")
    print("0️⃣  العودة للقائمة الرئيسية")
    
    choice = input("\n🎯 اختر رقم المكون: ").strip()
    
    if choice == "0":
        return
    elif choice in components:
        name, filename = components[choice]
        print(f"\n🚀 تشغيل {name}...")
        try:
            subprocess.run([sys.executable, filename])
        except KeyboardInterrupt:
            print(f"\n🛑 تم إيقاف {name}")
        except Exception as e:
            print(f"\n❌ خطأ في تشغيل {name}: {e}")
    else:
        print("❌ خيار غير صحيح")

def main():
    """الدالة الرئيسية"""
    print_banner()
    
    # فحص الملفات المطلوبة
    required_files = [
        "revolutionary_mother_equation.py",
        "complete_multi_layer_thinking_core.py",
        "complete_specialized_databases.py", 
        "enhanced_artistic_unit_fixed.py",
        "artistic_inference_interface.py"
    ]
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("❌ ملفات مفقودة:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n🔧 تأكد من وجود جميع ملفات النظام في نفس المجلد")
        return
    
    print("✅ جميع ملفات النظام موجودة")
    
    # بدء القائمة الرئيسية
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n🛑 تم إيقاف النظام")
    except Exception as e:
        print(f"\n❌ خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()

