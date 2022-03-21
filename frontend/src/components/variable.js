import { reactive } from 'vue'

export const variable = reactive({
    count: 0,
    increment() {
        this.count++
    }
})