<script lang="ts">
	import { onMount } from 'svelte';
	import { userStore } from '$lib/stores/userStore';
	import { userActivityStore } from '$lib/stores/userActivityStore';
	import Swiper from 'swiper';
	import 'swiper/css';
	import type { User } from '$lib/models/user.model';
	import type { UserActivity } from '$lib/models/userActivity.model';
	import JobPage from '$lib/components/jobPage.svelte';

	let swiper;

	let index = 0;
	let content = [null, null];

	let user: User;
	let userActivity: UserActivity;

	onMount(async () => {
		swiper = new Swiper('.swiper', {
			loop: true
		});

		content = [await getNextJob(), await getNextJob()];

		swiper.on('slideNextTransitionEnd', async () => {
			// dislike
			userActivityStore.update((ua: UserActivity) => ({
				...ua,
				dislikedJobs: [...ua.dislikedJobs, content[index]?.id]
			}));
			console.log(content, index);

			content[index] = await getNextJob();
			index = (index + 1) % 2;
		});

		swiper.on('slidePrevTransitionEnd', async () => {
			// like
			userActivityStore.update((ua: UserActivity) => ({
				...ua,
				likedJobs: [...ua.likedJobs, content[index]?.id]
			}));
			console.log(content, index);

			content[index] = await getNextJob();
			index = (index + 1) % 2;
		});

		userStore.subscribe((u: User) => {
			user = u;
		});

		userActivityStore.subscribe((ua: UserActivity) => {
			userActivity = ua;
		});
	});

	const getNextJob = async () => {
		const response = await fetch('http://localhost:5000/get_job', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ user, userActivity })
		});

		if (response.status === 200) {
			const data = await response.json();

			return data;
		} else {
			return null;
		}
	};
</script>

<svelte:head>
	<title>Work'd | Apply Now</title>
</svelte:head>
<div class="h-screen w-screen swiper">
	<div class="swiper-wrapper">
		<div class="bg-white swiper-slide">
			{#if content[0] !== null}
				<JobPage jobPosting={content[0]} />
			{:else}
				<div class="h-full w-full flex items-center justify-center">
					<h1 class="text-2xl font-display">No Jobs Available :/</h1>
				</div>
			{/if}
		</div>
		<div class="bg-white swiper-slide">
			{#if content[1] !== null}
				<JobPage jobPosting={content[1]} />
			{:else}
				<div class="h-full w-full flex items-center justify-center">
					<h1 class="text-2xl font-display">No Jobs Available :/</h1>
				</div>
			{/if}
		</div>
	</div>
</div>
