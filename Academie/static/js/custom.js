$(".js-height-full").height($(window).height());
$(".js-height-parent").each(function () {
	$(this).height($(this).parent().first().height());
});


// Fun Facts
function count($this) {
	var current = parseInt($this.html(), 10);
	current = current + 1; /* Where 50 is increment */

	$this.html(++current);
	if (current > $this.data('count')) {
		$this.html($this.data('count'));
	} else {
		setTimeout(function () {
			count($this)
		}, 50);
	}
}

$(".stat-timer").each(function () {
	$(this).data('count', parseInt($(this).html(), 10));
	$(this).html('0');
	count($(this));
});


$('.header').affix({
	offset: {
		top: 100,
		bottom: function () {
			return (this.bottom = $('.footer').outerHeight(true))
		}
	}
})

$(window).load(function () {
	$("#preloader").on(500).fadeOut();
	$(".preloader").on(600).fadeOut("slow");
});



	// Toggle password visibility
	const passwordToggle = document.getElementById('passwordToggle');
	const passwordInput = document.querySelector('input[type="password"]');

	if (passwordToggle && passwordInput) {
	passwordToggle.addEventListener('click', function () {
		const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
		passwordInput.setAttribute('type', type);

		const eyeIcon = this.querySelector('i');
		if (type === 'text') {
			eyeIcon.className = 'fas fa-eye-slash';
			this.setAttribute('title', 'مخفی کردن رمز عبور');
		} else {
			eyeIcon.className = 'fas fa-eye';
			this.setAttribute('title', 'نمایش رمز عبور');
		}
	});
}

	// Form submission with loading state
	const form = document.querySelector('.auth-form');
	const submitBtn = document.querySelector('.submit-btn');

	if (form && submitBtn) {
	form.addEventListener('submit', function (e) {
		submitBtn.classList.add('loading');

		// Simulate loading for demo (remove in production)
		setTimeout(() => {
			submitBtn.classList.remove('loading');
		}, 2000);
	});
}

	// Social login buttons
	const socialButtons = document.querySelectorAll('.social-btn');

	socialButtons.forEach(button => {
	button.addEventListener('click', function () {
		const socialType = this.classList.contains('google') ? 'Google' : 'GitHub';

		// Add click animation
		this.style.transform = 'scale(0.95)';
		setTimeout(() => {
			this.style.transform = '';
		}, 200);

		console.log(`Login with ${socialType} clicked`);
		// Add your social login logic here
	});
});

	// Form validation on blur
	const inputs = document.querySelectorAll(
  '.auth-form input[type="email"], .auth-form input[type="password"], .auth-form input[type="text"]'
);


	inputs.forEach(input => {
	input.addEventListener('blur', function () {
		if (this.value.trim() === '') {
			this.style.borderColor = 'rgba(255, 255, 255, 0.1)';
		} else if (this.checkValidity()) {
			this.style.borderColor = '#10b981';
		} else {
			this.style.borderColor = '#ef4444';
		}
	});
});

	// Auto-focus on email field if empty
	window.addEventListener('load', function() {
	const emailInput = document.querySelector('input[type="email"]');
	if (emailInput && emailInput.value === '') {
	emailInput.focus();
}
});

	// Add floating label effect
	const labels = document.querySelectorAll('.form-label');

	labels.forEach(label => {
	const input = document.getElementById(label.getAttribute('for'));

	if (input) {
	input.addEventListener('focus', function() {
	label.style.color = '#8b5cf6';
	label.querySelector('i').style.color = '#8b5cf6';
});

	input.addEventListener('blur', function() {
	if (this.value === '') {
	label.style.color = '#b0b0c0';
	label.querySelector('i').style.color = '#8b5cf6';
}
});
}
});

	// Remember me checkbox animation
	const rememberCheckbox = document.querySelector('input[name="remember"]');

	if (rememberCheckbox) {
	rememberCheckbox.addEventListener('change', function () {
		const checkmark = this.nextElementSibling;
		if (this.checked) {
			checkmark.style.transform = 'translateY(-50%) scale(1.1)';
			setTimeout(() => {
				checkmark.style.transform = 'translateY(-50%) scale(1)';
			}, 200);
		}
	});
}

