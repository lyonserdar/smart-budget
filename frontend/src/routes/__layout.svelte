<script>
  import Header from "$lib/header/Header.svelte";
  import { Content, Grid } from "carbon-components-svelte";
  import "carbon-components-svelte/css/g10.css";
</script>

<Header />

<Content>
  <Grid>
    <slot />
  </Grid>
</Content>

<style>
</style>
