// userActivityStore.ts
import type { UserActivity } from '$lib/models/userActivity.model';
import { persistToLocalStorage } from '../localStorageUtil';

// Initial value for user activity
const initialUserActivity: UserActivity = {
	likedJobs: [],
	dislikedJobs: []
};

// Create a writable store that persists to localStorage
export const userActivityStore = persistToLocalStorage<UserActivity>(
	'userActivityStore',
	initialUserActivity
);
