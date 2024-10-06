<script lang="ts">
	import { userStore } from '$lib/stores/userStore';
	import { type User } from '$lib/models/user.model';
	import { onMount } from 'svelte';

	let email: string = '';
	let error: string = '';

	// Subscribe to userStore
	userStore.subscribe((user: User) => {
		email = user.email;
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		if (!email) {
			error = 'Email is required.';
		} else {
			userStore.update((user: User) => ({ ...user, email })); // Update store
			error = '';
			location.href = '/onboarding/ethnicity'; // Navigate to next page
		}
	};
</script>

<form
	on:submit={handleNext}
	class="flex flex-col items-center justify-between h-full w-full space-y-6"
>
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">Enter Your Email</h1>
		<input
			bind:value={email}
			type="email"
			name="email"
			placeholder="Email"
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
