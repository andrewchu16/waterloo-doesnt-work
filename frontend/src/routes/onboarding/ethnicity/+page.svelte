<script lang="ts">
	import { userStore } from '$lib/stores/userStore';
	import { type User } from '$lib/models/user.model';
	import { onMount } from 'svelte';

	let ethnicity: string[] = [];
	let error: string = '';

	onMount(() => {
		// Subscribe to userStore
		userStore.subscribe((user: User) => {
			ethnicity = user.ethnicity;
			console.log(ethnicity)
		});
	});

	const handleNext = (event: Event) => {
		event.preventDefault();
		if (ethnicity.length === 0) {
			error = 'Please select at least one ethnicity.';
		} else {
			userStore.update((user: User) => ({ ...user, ethnicity })); // Update store
			error = '';
			location.href = '/onboarding/resume'; // Navigate to next page
		}
	};

	// Toggle function to handle checkbox selection
	const toggleEthnicity = (value: string) => {
		if (ethnicity.includes(value)) {
			ethnicity = ethnicity.filter((e) => e !== value);
		} else {
			ethnicity = [...ethnicity, value];
		}
	};
</script>

<form
	on:submit={handleNext}
	class="flex flex-col items-center justify-between h-full w-full space-y-6"
>
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">Select Your Ethnicity</h1>

		<label>
			<input
				type="checkbox"
				checked={ethnicity.includes('Asian')}
				on:change={() => toggleEthnicity('Asian')}
			/>
			Asian
		</label>

		<label>
			<input
				type="checkbox"
				checked={ethnicity.includes('Black or African American')}
				on:change={() => toggleEthnicity('Black or African American')}
			/>
			Black or African American
		</label>

		<label>
			<input
				type="checkbox"
				checked={ethnicity.includes('Hispanic or Latino')}
				on:change={() => toggleEthnicity('Hispanic or Latino')}
			/>
			Hispanic or Latino
		</label>

		<label>
			<input
				type="checkbox"
				checked={ethnicity.includes('White')}
				on:change={() => toggleEthnicity('White')}
			/>
			White
		</label>

		<label>
			<input
				type="checkbox"
				checked={ethnicity.includes('Other')}
				on:change={() => toggleEthnicity('Other')}
			/>
			Other
		</label>

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
