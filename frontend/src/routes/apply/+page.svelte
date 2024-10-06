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

	onMount(() => {
		swiper = new Swiper('.swiper', {
			loop: true
		});

		swiper.on('slideNextTransitionEnd', () => {
			// dislike
			userActivityStore.update((ua: UserActivity) => ({
				...ua,
				dislikedJobs: [...ua.dislikedJobs, content[index]?.id]
			}));

			setTimeout(async () => {
				content[index] = await getNextJob();
			}, 100);

			index = (index + 1) % 2;
            console.log(userActivity);
		});

		swiper.on('slidePrevTransitionEnd', () => {
			// like
			userActivityStore.update((ua: UserActivity) => ({
				...ua,
				likedJobs: [...ua.likedJobs, content[index]?.id]
			}));

			setTimeout(async () => {
				content[index] = await getNextJob();
			}, 100);
			index = (index + 1) % 2;
            console.log(userActivity);
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
		<div class="bg-primary swiper-slide">
			{#if content[0] !== null}
				<JobPage jobPosting={content[0]} />
			{:else}NO JOB 1{/if}
		</div>
		<div class="bg-secondary swiper-slide">
			{#if content[1] !== null}
				<JobPage jobPosting={content[1]} />
			{:else}NO JOB 2{/if}
		</div>
	</div>
</div>
