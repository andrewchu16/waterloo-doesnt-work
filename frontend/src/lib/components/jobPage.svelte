<script lang="ts">
	import type { Job } from '$lib/models/job.model';

	export let jobPosting: Job;
</script>

<div class="flex flex-col items-center justify-between h-full w-full space-y-6">
	<div class="w-full flex flex-col gap-2 px-2 py-8 flex-grow">
        <div class="flex flex-col gap-1">
            <h1 class="text-2xl font-display font-bold">{jobPosting.companyName}</h1>
            <div>
                <p class="truncate w-full">{jobPosting.jobTitle}</p>
                <p class="italic truncate w-full">{jobPosting.location}</p>
            </div>
        </div>
		<p>{jobPosting.description}</p>
        <img src={jobPosting.picture} alt={jobPosting.jobTitle} />
	</div>
</div>
