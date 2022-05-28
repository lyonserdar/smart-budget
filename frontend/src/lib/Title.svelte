<script>
  import { Column, Row } from "carbon-components-svelte";
  export let text = "";
</script>

<Row padding>
  <Column>
    <h1>{text}</h1>
  </Column>
</Row>
