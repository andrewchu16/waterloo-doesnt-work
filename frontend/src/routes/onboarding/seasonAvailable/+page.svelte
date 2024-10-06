<script lang="ts">
	import { userStore, type User, type SeasonAvailable } from '$lib/stores/userStore';
	import { onMount } from 'svelte';

	let seasonAvailable: SeasonAvailable = 'winter 2025';
	const seasons: SeasonAvailable[] = ['winter 2025', 'summer 2025', 'fall 2025', 'spring 2025'];

	// Subscribe to userStore
	userStore.subscribe((user: User) => {
		seasonAvailable = user.seasonAvailable;
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		userStore.update((user: User) => ({ ...user, seasonAvailable })); // Update store
		location.href = '/apply'; // Navigate to the apply page
	};
</script>

<form
	on:submit={handleNext}
	class="flex flex-col items-center justify-between h-full w-full space-y-6"
>
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">Select Your Availability</h1>
		<select bind:value={seasonAvailable} class="py-2 px-4 border border-gray-300 rounded-lg w-full">
			{#each seasons as season}
				<option value={season}>{season}</option>
			{/each}
		</select>
	</div>
	<button
		type="submit"
		class="py-3 w-full bg-primary rounded-full text-white hover:brightness-75 text-xl"
	>
		Complete
	</button>
</form>
