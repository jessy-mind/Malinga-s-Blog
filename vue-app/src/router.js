import {createWebHistory, createRouter} from "vue-router";

import MalingaPage from "./apps/MalingaPage.vue";
import BlogPage from "./apps/BlogPage.vue";


const routes = [
{
	path:'/malinga',
	component:MalingaPage
},
{
	path:'/blog',
	component: BlogPage
}
];

const router = createRouter({
	history:createWebHistory(),
	routes:routes,
});


export default router;