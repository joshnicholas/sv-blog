<script context="module">
	// import { dirname } from 'path';
	// import { fileURLToPath } from 'url';
	// const loc = window.location.pathname;
	// const loc = process.cwd()
	// const __filename = fileURLToPath(import.meta.url);
	// var loc = dirname(__filename);
	// import { page } from '$lib/assets/js/store';
  // import { currentPage, isMenuOpen } from '$lib/assets/js/store'


	// console.log(currentPage)
	// console.log("pageo: ", page)

	// console.log("Loc: ", loc)
	// console.log(process.cwd()) 

	var loc = '/words'

	export const load = async ({ fetch }) => {
		const postRes = await fetch(`/api${loc}.json`)
		const { posts } = await postRes.json()

    const totalRes = await fetch(`/api${loc}/count.json`)
    const { total } = await totalRes.json()

		return {
			props: { posts, total }
		}
	}


	// console.log(loc)
  // import { isMenuOpen } from '$lib/assets/js/store'
	// console.log($isMenuOpen)

	// export let currentPage
	// const isCurrentPage = (page) => page == currentPage

	// console.log(page)
</script>


<script>
  import PostsList from '$lib/components/PostsList.svelte'
  import Pagination from '$lib/components/Pagination.svelte'
	import { siteDescription } from '$lib/config'
	export let posts
  export let total
</script>


<svelte:head>
	<title>Blog</title>
	<meta data-key="description" name="description" content={siteDescription}>
</svelte:head>


<h1>Blog</h1>

<PostsList {posts} />

<Pagination currentPage={1} totalPosts={total} />