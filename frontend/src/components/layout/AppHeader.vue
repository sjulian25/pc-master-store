<template>
    <header class="header">
        <Logo />
        <Navbar />
        <div id="sub-header">
            <Search />
            <Login />
        </div>
    </header>
</template>

<script setup>
import Logo from "@/components/header/Logo.vue"
import Navbar from "@/components/header/Navbar.vue"
import Search from "@/components/header/Search.vue"
import Login from "@/components/header/Login.vue"
</script>

<style src="../../assets/css/Header/header.css" scoped>
</style>