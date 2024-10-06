// userStore.ts
import { persistToLocalStorage } from '../localStorageUtil';

export type SeasonAvailable = 'winter 2025' | 'summer 2025' | 'fall 2025' | 'spring 2025';

export interface User {
	name: string;
	email: string;
	ethnicity: string[];
	resumeSummary: string;
	education: string;
	graduationYear: number | null;
	seasonAvailable: SeasonAvailable;
}

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
