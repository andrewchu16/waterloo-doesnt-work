<main class="bg-primary h-svh w-screen flex flex-col items-center justify-center">
	<div class="py-40 text-center onboarding-header">
		<h1 class="font-display text-5xl text-white display-spacing suffix-animation">work</h1>
		<h2 class="pt-4 text-white">Giving you less work, more day.</h2>
	</div>
	<a
		class="py-3 px-4 bg-white rounded-full text-primary hover:bg-neutral-200 get-started-button"
		href="/onboarding">Next</a
	>
</main>

<svelte:head>
	<title>Workd</title>
</svelte:head>
<style>
	.suffix-animation::after {
		animation: delete-suffix 4s alternate-reverse infinite;
		content: 'day';
		text-decoration-skip-ink: none;
		@apply text-white;
	}

	@keyframes delete-suffix {
		0% {
			content: 'day?';
			@apply text-white;
		}

		40% {
			content: 'day?';
			@apply text-white;
		}

		45% {
			content: 'day';
		}

		50% {
			content: 'da';
		}

		55% {
			content: 'd';
		}

		100% {
			content: 'd';
			@apply text-secondary;
		}
	}
</style>
