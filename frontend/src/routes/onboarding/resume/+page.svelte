<script lang="ts">
	import { userStore, type User } from '$lib/stores/userStore';
	import { onMount } from 'svelte';

	let resumeSummary: string = '';
	let error: string = '';

	// Subscribe to userStore
	userStore.subscribe((user: User) => {
		resumeSummary = user.resumeSummary;
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		if (!resumeSummary) {
			error = 'Resume summary is required.';
		} else {
			userStore.update((user: User) => ({ ...user, resumeSummary })); // Update store
			error = '';
			location.href = '/onboarding/education'; // Navigate to next page
		}
	};
</script>

<form
	on:submit={handleNext}
	class="flex flex-col items-center justify-between h-full w-full space-y-6"
>
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">Enter Your Resume Summary</h1>
		<textarea
			bind:value={resumeSummary}
			placeholder="Write a brief summary of your resume..."
			class="py-2 px-4 border border-gray-300 rounded-lg w-full"
		></textarea>
		{#if error}
			<p class="text-red-500">{error}</p>
		{/if}
	</div>
	<button
		type="submit"
		class="py-3 w-full bg-primary rounded-full text-white hover:brightness-75 text-xl"
	>
		Next
	</button>
</form>
