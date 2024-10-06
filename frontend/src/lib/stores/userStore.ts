// userStore.ts
import { persistToLocalStorage } from '../localStorageUtil';
import { type User } from '../models/user.model';

// Initial value for the user
const initialUser: User = {
	name: '',
	ethnicity: [],
	resumeSummary: '',
	education: '',
	graduationYear: null,
	seasonAvailable: 'winter 2025',
	email: ''
};

// Create a writable store that persists to localStorage
export const userStore = persistToLocalStorage<User>('userStore', initialUser);
