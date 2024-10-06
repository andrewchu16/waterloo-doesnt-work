<script lang="ts">
	import { userStore } from '$lib/stores/userStore';
	import { type User } from '$lib/models/user.model';
	import { onMount } from 'svelte';

	let education: string = '';
	let error: string = '';
	let graduationYearStr: string = '';

	// Subscribe to userStore
	userStore.subscribe((user: User) => {
		education = user.education;
		graduationYearStr = user.graduationYear ? user.graduationYear.toString() : '';
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		if (!education) {
			error = 'Education is required.';
		} else {
			const graduationYear: number | null = graduationYearStr ? parseInt(graduationYearStr) : null;
			userStore.update((user: User) => ({ ...user, education, graduationYear })); // Update store
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
		<h1 class="text-2xl font-display">Graduating Year (if applicable)</h1>
		<input
			bind:value={graduationYearStr}
			type="text"
			placeholder="Graduating Year"
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
