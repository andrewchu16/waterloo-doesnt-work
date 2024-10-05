import { writable, type Writable } from 'svelte/store';

export function persistToLocalStorage<T>(key: string, initialValue: T): Writable<T> {
	// Check if localStorage is available (i.e., the code is running in the browser)
	const isBrowser = typeof window !== 'undefined' && window.localStorage;

	// Get the stored value from localStorage if available, otherwise use the initial value
	const storedValue = isBrowser ? localStorage.getItem(key) : null;
	const parsedValue = storedValue ? JSON.parse(storedValue) : initialValue;

	// Create a Svelte writable store
	const store = writable<T>(parsedValue);

	// Subscribe to store changes and update localStorage if available
	if (isBrowser) {
		store.subscribe((value) => {
			localStorage.setItem(key, JSON.stringify(value));
		});
	}

	return store;
}
