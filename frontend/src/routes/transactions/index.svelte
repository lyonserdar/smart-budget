<script>
  import Title from "$lib/Title.svelte";
  import {
    Button,
    DataTable,
    Toolbar,
    ToolbarContent,
    ToolbarMenu,
    ToolbarMenuItem,
    ToolbarSearch,
  } from "carbon-components-svelte";
</script>

<svelte:head>
  <title>Transactions</title>
  <meta name="description" content="My transactions" />
</svelte:head>

<Title text="Transactions" />

<DataTable
  title="Transaction History"
  description="My transaction history"
  headers={[
    { key: "name", value: "Name" },
    { key: "amount", value: "Amount" },
    { key: "date", value: "Date" },
    { key: "bucket", value: "Bucket" },
  ]}
  rows={[
    {
      id: 1,
      name: "one",
      amount: "$120.00",
      date: "12/12/2022",
      bucket: "Personal",
    },
    {
      id: 2,
      name: "two",
      amount: "$340.00",
      date: "12/12/2022",
      bucket: "Health",
    },
    {
      id: 3,
      name: "three",
      amount: "$340.00",
      date: "12/12/2022",
      bucket: "Health",
    },
    {
      id: 4,
      name: "four",
      amount: "$340.00",
      date: "12/12/2022",
      bucket: "Health",
    },
    {
      id: 5,
      name: "five",
      amount: "$340.00",
      date: "12/12/2022",
      bucket: "Health",
    },
  ]}
>
  <Toolbar>
    <ToolbarContent>
      <ToolbarSearch />
      <ToolbarMenu>
        <ToolbarMenuItem primaryFocus>Primary</ToolbarMenuItem>
        <ToolbarMenuItem>Item</ToolbarMenuItem>
        <ToolbarMenuItem hasDivider danger>Item 2</ToolbarMenuItem>
      </ToolbarMenu>
      <Button>Add transaction</Button>
    </ToolbarContent>
  </Toolbar>
</DataTable>

<style>
</style>
