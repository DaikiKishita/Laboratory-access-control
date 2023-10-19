<template>
    <div class="base">
        <a class="name">名前</a>
        <div class="Input_name">
            <a-input v-model:value="userName" placeholder="Enter your name" required>
            <template #prefix>
                <user-outlined />
            </template>
            <template #suffix>
                <a-tooltip title="Extra information">
                    <info-circle-outlined style="color: rgba(0, 0, 0, 0.45)" />
                </a-tooltip>
            </template>
            </a-input>
        </div>
        <a-button type="primary">送信</a-button>
    </div>
</template>

<script>

</script>

<style>
.base{
    margin: auto;
    text-align: center;
    background-color: silver;
    padding-top: 10px;
    padding-bottom: 10px;
}
.Input_name{
    margin: auto;
    width: 30%;
    margin-bottom: 10px;
}
.name{
    size: 120%;
}
</style>
