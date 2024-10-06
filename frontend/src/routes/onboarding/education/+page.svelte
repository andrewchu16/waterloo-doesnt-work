<script lang="ts">
	import { userStore, type User } from '$lib/stores/userStore';
	import { onMount } from 'svelte';

	let education: string = '';
	let error: string = '';

	// Subscribe to userStore
	userStore.subscribe((user: User) => {
		education = user.education;
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		if (!education) {
			error = 'Education is required.';
		} else {
			userStore.update((user: User) => ({ ...user, education })); // Update store
			error = '';
			location.href = '/onboarding/seasonAvailable'; // Navigate to next page
		}
	};
</script>

<form
	on:submit={handleNext}
	class="flex flex-col items-center justify-between h-full w-full space-y-6"
>
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">Enter Your Education</h1>
		<input
			bind:value={education}
			type="text"
			placeholder="Education"
			class="py-2 px-4 border border-gray-300 rounded-lg w-full"
		/>
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
