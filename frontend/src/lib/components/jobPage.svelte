<script lang="ts">
	import type { Job } from '$lib/models/job.model';

	export let jobPosting: Job;
</script>

<div class="flex flex-col items-center justify-between h-full w-full space-y-6">
	<div class="w-full flex flex-col gap-4 items-center justify-center flex-grow">
		<h1 class="text-2xl font-display">{jobPosting.companyName}</h1>
		<p>{jobPosting.jobTitle}</p>
		<p>{jobPosting.description}</p>
        <img src={jobPosting.picture} alt={jobPosting.jobTitle} />
	</div>
</div>
