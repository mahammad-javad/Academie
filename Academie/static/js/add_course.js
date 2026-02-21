document.addEventListener("DOMContentLoaded", function () {
    const requestBtn = document.getElementById("request-course-btn");
    if (!requestBtn) return;

    requestBtn.addEventListener("click", function (e) {
        e.preventDefault();

        Swal.fire({
            title: 'آیا مطمئن هستید؟',
            text: "می‌خواهید در این دوره شرکت کنید؟",
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'بله، مطمئنم',
            cancelButtonText: 'لغو'
        }).then((result) => {
            if (result.isConfirmed) {
                fetch(requestBtn.dataset.url, {
                    method: 'POST',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                })
                .then(response => {
                    if (response.status === 401) {
                        // کاربر لاگین نیست → هدایت به صفحه لاگین
                        window.location.href = '/accounts/login/';
                        return;
                    }
                    if (!response.ok) throw new Error('مشکلی پیش آمد.');
                    return response.json();
                })
                .then(data => {
                    if (!data) return; // اگر redirect شد، دیگه کاری نکن
                    Swal.fire({
                        icon: 'success',
                        title: 'پیغام',
                        text: data.message,
                    });
                })
                .catch(error => {
                    Swal.fire({
                        icon: 'error',
                        title: 'خطا',
                        text: error.message,
                    });
                });
            }
        });

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.startsWith(name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    });
});
