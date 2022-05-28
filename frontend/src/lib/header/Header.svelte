<script>
  import {
    Header,
    HeaderAction,
    HeaderNav,
    HeaderNavItem,
    HeaderNavMenu,
    HeaderPanelLink,
    HeaderPanelLinks,
    HeaderUtilities,
    SideNav,
    SideNavItems,
    SideNavLink,
    SideNavMenu,
    SideNavMenuItem,
    SkipToContent,
  } from "carbon-components-svelte";
  import { UserAvatarFilledAlt } from "carbon-icons-svelte";
  //   import { page } from "$app/stores";
  let isSideNavOpen = false;
</script>

<Header
  company="smart-budget"
  platformName="dev"
  href="/"
  bind:isSideNavOpen
  expandedByDefault={false}
>
  <div slot="skip-to-content"><SkipToContent /></div>
  <HeaderNav>
    <HeaderNavItem text="Transactions" href="/transactions" />
    <HeaderNavMenu text="Menu">
      <HeaderNavItem text="Test" />
    </HeaderNavMenu>
    <HeaderNavItem text="About" href="/about" />
  </HeaderNav>
  <HeaderUtilities>
    <HeaderAction icon={UserAvatarFilledAlt}>
      <HeaderPanelLinks>
        <HeaderPanelLink>Account</HeaderPanelLink>
        <HeaderPanelLink>Settings</HeaderPanelLink>
        <HeaderPanelLink>Login</HeaderPanelLink>
        <HeaderPanelLink>Logout</HeaderPanelLink>
      </HeaderPanelLinks>
    </HeaderAction>
  </HeaderUtilities>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavLink text="Transactions" href="/transactions" />
    <SideNavMenu text="Menu">
      <SideNavMenuItem text="Test" />
    </SideNavMenu>
    <SideNavLink text="About" href="/about" />
  </SideNavItems>
</SideNav>

<!-- <nav>
    <ul>
      <li class:active={$page.url.pathname === "/"}>
        <a sveltekit:prefetch href="/">Home</a>
      </li>
      <li class:active={$page.url.pathname === "/about"}>
        <a sveltekit:prefetch href="/about">About</a>
      </li>
      <li class:active={$page.url.pathname === "/todos"}>
        <a sveltekit:prefetch href="/todos">Todos</a>
      </li>
    </ul>
  </nav> -->
<style>
</style>
