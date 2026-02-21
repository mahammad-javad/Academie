document.addEventListener('DOMContentLoaded', function () {
    // اضافه کردن افکت hover بهتر
    const selectElement = document.querySelector('.modern-select select');
    const infoBox = document.querySelector('.pagination-info-dark');

    if (selectElement) {
        selectElement.addEventListener('focus', function () {
            this.parentElement.classList.add('focused');
        });

        selectElement.addEventListener('blur', function () {
            this.parentElement.classList.remove('focused');
        });
    }

    if (infoBox) {
        infoBox.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-2px)';
        });

        infoBox.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    }

    // تنظیم auto-submit برای select
    document.querySelectorAll('.modern-select select').forEach(select => {
        select.addEventListener('change', function () {
            // اضافه کردن افکت لودینگ
            const originalText = this.parentElement.querySelector('::before')?.content;
            if (this.parentElement.querySelector('::before')) {
                this.parentElement.querySelector('::before').style.content = '"⏳"';
                setTimeout(() => {
                    this.parentElement.querySelector('::before').style.content = originalText;
                }, 500);
            }

            // ارسال فرم
            this.form.submit();
        });
    });
});
