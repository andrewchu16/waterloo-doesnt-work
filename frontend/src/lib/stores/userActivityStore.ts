// userActivityStore.ts
import { persistToLocalStorage } from '../localStorageUtil';

// Define the User Activity interface
export interface UserActivity {
	LikedJobs: string[];
	DislikedJobs: string[];
}

// Initial value for user activity
const initialUserActivity: UserActivity = {
	LikedJobs: [],
	DislikedJobs: []
};

// Create a writable store that persists to localStorage
export const userActivity = persistToLocalStorage<UserActivity>(
	'userActivityStore',
	initialUserActivity
);
