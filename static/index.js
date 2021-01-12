// import {
//     main_content,
//     get_group_row_element_for_all_group_list
// } from "./components/main_content";
// var content = required("./components/main_content.js")
// console.log(content)
$(document).ready(() => {

    $.when(
        $.ajax({
            url: "components\\main_content.js",
            dataType: "script",
            crossDomain: true
        }),
        $.ajax({
            url: "components\\group_details.js",
            dataType: "script",
            crossDomain: true
        }),
        $.Deferred(function (deferred) {
            $(deferred.resolve);
        })
    ).done(function () {

        init_page()
    });

});

init_page = () => {
    //get user and main data from server
    user_name = "sara"
    user_mail = "sm@1234.com"
    user_img_path = "assets\\img\\client-img4.png"
    num_of_app_visitors = 999
    num_of_visitors_likes = 567
    number_of_groups_created = 100
    list_of_recent_groups = [{
            group_id: 111,
            product_name: "yoyo stroller",
            num_of_subscibers: 8,
            popularity: 50
        },
        {
            group_id: 111,
            product_name: "yoyo stroller",
            num_of_subscibers: 8,
            popularity: 50
        },
        {
            group_id: 111,
            product_name: "yoyo stroller",
            num_of_subscibers: 8,
            popularity: 50
        }
    ]
    console.log("hello")



    //render
    $("#group_details").addClass("hidden")
    $("#router-outlet").html(main_content + table_of_groups)
    $("#user_name").text(user_name)
    $("#user_mail").text(user_mail)
    $(".user_img_path").attr("src", user_img_path)
    $("#num_of_app_visitors").text(num_of_app_visitors)
    $("#num_of_visitors_likes").text(num_of_visitors_likes)
    $("#number_of_groups_created").text(number_of_groups_created)

    let line_all_recent_groups = ""
    list_of_recent_groups.forEach(G => {
        // onsole.log(G)
        line_all_recent_groups += get_group_row_element_for_all_group_list(G)
    });
    $(".rows_of_recent_groups_table").html(line_all_recent_groups)




    //event listeners
    $("#btn_view_all_groups_in_list").click(() => route_all_group_list())
    $(".group_row_in_table").click((e) => route_to_group_details(e.currentTarget.id))
    $("#btn_subscribe").click((e) => subscribe_user_to_group(e.currentTarget.id))
    $("#link_to_user_profile").click( () => console.log("clicked on profile"))
    $("#link_show_groups_by_category").click(() => console.log("group by category"))
    $("#link_show_all_groups").click(route_all_group_list)
    $("#link_to_your_groups").click(route_all_group_list)
    $("#link_to_create_new_group").click(route_to_create_new_group)
}



subscribe_user_to_group = (group_id) => {
    console.log("user subscribes to group")
}



route_to_create_new_group = () => {
    $("#router-outlet").html(create_new_group)
}


route_all_group_list = () => {
    console.log("view all was clicked")
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")

    //get data from server or from browser
    all_groups = list_of_recent_groups

    //render
    let line_all_recent_groups = ""
    all_groups.forEach(G => {
        console.log(G)
        line_all_recent_groups += get_group_row_element_for_all_group_list(G)
    });
    console.log(line_all_recent_groups)
    $(".rows_of_recent_groups_table").html(line_all_recent_groups)



    //render
    $("#router-outlet").html(table_of_groups)
}





route_to_group_details = (group_id) => {
    console.log("group_details", group_details)
    //get group details from server , includes imgs
    num_of_subscribers = 8
    path_imgs_arr = [
        "assets\img\slick1.jpg", 
        "assets\img\slick2.jpg", 
        "assets\img\slick3.jpg", 
        "assets\img\slick4.jpg", 
        "assets\img\slick6.jpg", 
        "assets\img\slick7.jpg"
    ]
    short_description_of_group = "yoyo stroller"
    brand_of_group_in_details = "yoyo"
    range_sum_for_group_product = "10.00$-50.00$"
    long_decription_of_group = "the best stroller for any child and baby in any age.... :), the best stroller for any child and baby in any age.... :), the best stroller for any child and baby in any age.... :), the best stroller for any child and baby in any age.... :), the best stroller for any child and baby in any age.... :), the best stroller for any child and baby in any age.... :)"


    //render
    $("#router-outlet").addClass("hidden")
    imgs_html_for_group_details = ""
    path_imgs_arr.forEach(path => imgs_html_for_group_details += render_img({img_path:path}))
    // $(".group_details_imgs_of_product").html(imgs_html_for_group_details)
    $("#product_details_num_of_subscibers").html(num_of_subscribers)
    $("#short_description_of_group").html(short_description_of_group)
    $("#brand_of_group_in_details").html(brand_of_group_in_details)
    $("#range_sum_for_group_product").html(range_sum_for_group_product)
    $("#long_decription_of_group").html(long_decription_of_group)
    $("#group_details").removeClass("hidden")
}



const render_img = _.template(`<img src="<%=img_path%>" alt="">`);