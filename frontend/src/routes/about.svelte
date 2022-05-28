<script context="module">
  import { browser, dev } from "$app/env";
  import { Link } from "carbon-components-svelte";
  import Title from "../lib/Title.svelte";

  // we don't need any JS on this page, though we'll load
  // it in dev so that we get hot module replacement...
  export const hydrate = dev;

  // ...but if the client-side router is already loaded
  // (i.e. we came here from elsewhere in the app), use it
  export const router = browser;

  // since there's no dynamic data here, we can prerender
  // it so that it gets served as a static asset in prod
  export const prerender = true;
</script>

<svelte:head>
  <title>About</title>
  <meta name="description" content="About this app" />
</svelte:head>

<Title text="About" />

<p>
  This is a budget app that I (<Link inline href="https://github.com/lyonserdar"
    >lyonserdar</Link
  >) mainly made for myself. But You can use it too! This is an open sourced
  project. (<Link inline href="https://github.com/lyonserdar/smart-budget"
    >Github</Link
  >)
</p>
<p>
  This app is built using Pyhton/FastAPI and SvelteKit. It also used Postgresql.
</p>

<style>
</style>
