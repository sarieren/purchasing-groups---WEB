// import {
//     main_content,
//     get_group_row_element_for_all_group_list
// } from "./components/main_content";
// var content = required("./components/main_content.js")
// console.log(content)
$(document).ready(() => {

    // $("#loader").css('display', 'block')
    $.when(
        $.ajax({
            url: "components\\main_content.js",
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
    user_name = document.cookie.split("username=")[1]
    $.get("/users/" + user_name, (res) => {
        console.log("user", res.user_mail)
        // user_mail = res.user_mail
        user_img_path = "assets\\img\\client-img4.png"
        $("#user_name").text(user_name)
        $("#user_mail").text(res["user_mail"])
        $(".user_img_path").attr("src", user_img_path)
    })
    
    num_of_app_visitors = 999
    num_of_visitors_likes = 567
    number_of_groups_created = 100

    //get groups and categories data from server
    list_all_groups = []
    list_all_categories = []
    cat_ob = {}
    __title_for_category_prt = "Some of Exist Categories"
    __secondary_title_for_category_part = "categories"

    $.when(
        
        $.get("/categories", function (data, status) {
            console.log(typeof (data))
            list_all_categories = JSON.parse(data)
            for(let cat of list_all_categories)
                cat_ob[cat.id] = cat.name


                $.get("/groups", function (data, status) {
                    console.log(typeof (data))
        
                    list_all_groups = JSON.parse(data).map(G => ({
                        group_id: G.id_,
                        group_name: G.group_name,
                        num_of_subscibers: 8,
                        item_name: G.item_name,
                        max_price: G.max_price,
                        manager: G.manager,
                        category: cat_ob[G.category_id],
                        end_data: G.end_data,
                        description_group: G.description_group
        
                    }))
                    list_all_groups.sort(compare_by_date);
                    console.log(list_all_groups)
                })
        }),

    ).done(function () {

        $("#group_details").addClass("hidden")
        $("#router-outlet").removeClass("hidden")

        //render
        let content = categories_component.format("Some Categories", "View All", "route_to_all_categories()")
        content += table_of_groups.format("Recent Groups", "View All","recent",  "route_to_view_all_groups()")
        // console.log(categories)
        content = $.parseHTML(content  + main_content)
        $("#router-outlet").append(content)
        
        $("#num_of_app_visitors").text(num_of_app_visitors)
        $("#num_of_visitors_likes").text(num_of_visitors_likes)
        $("#number_of_groups_created").text(number_of_groups_created)

        elem_all_groups = ""
        list_all_groups.forEach(G => {
            onsole.log(G)
            elem_all_groups += get_group_row_element_for_all_group_list(G)
        });
        elem_all_groups = $.parseHTML(elem_all_groups)
        $("#rows_of_recent_groups_table_recent").append(elem_all_groups)

        list_all_categories.forEach(cat => {
            const url = render_random_img(cat.name)

            const cat_ele = $.parseHTML(category_card.format(cat.name, cat.name, cat.id, url))
            $(".container_for_categories").append(cat_ele)
        })



        //event listeners
        $("#btn_view_all_groups_in_list").click(() => route_to_view_all_groups())
        // $(".group_row_in_table").click((e) => route_to_group_details(e.currentTarget.id))
        $("#btn_subscribe").click((e) => subscribe_user_to_group(e.currentTarget.id))
        $("#link_to_user_profile").click(() => console.log("clicked on profile"))
        $("#link_show_groups_by_category").click(() => route_to_all_categories)
        $("#link_show_all_groups").click(route_to_view_all_groups)
        $("#link_to_your_groups").click(route_to_view_your_groups)
        $("#link_to_create_new_group").click(route_to_create_new_group)

        $("#logo").click(route_to_home_page)
        // $("#loader").css('display', 'none')

    });


}


route_to_home_page = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    let content = categories_component.format("Categories", "View All", "route_to_all_categories()")
    content += table_of_groups.format("Recent Groups", "View All","recent",  "route_to_view_all_groups()")
    content = $.parseHTML(content + main_content)
    $("#router-outlet").append(content)
    $(".user_img_path").attr("src", user_img_path)
    $("#num_of_app_visitors").text(num_of_app_visitors)
    $("#num_of_visitors_likes").text(num_of_visitors_likes)
    $("#number_of_groups_created").text(number_of_groups_created)
    console.log("all group", elem_all_groups)
    $("#rows_of_recent_groups_table_recent").html(elem_all_groups)

    list_all_categories.forEach(cat => {
        const url = render_random_img(cat.name)
        const cat_ele = $.parseHTML(category_card.format(cat.name, cat.name, cat.id, url))
        $(".container_for_categories").append(cat_ele)
    })
}

subscribe_user_to_group = (group_id) => {
    console.log("user subscribes to group")
}



route_to_create_new_group = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    let content = $.parseHTML(new_group_form({"categories":list_all_categories}))
    $("#router-outlet").append(content)
    // $("#router-outlet").html(create_new_group)

    $("#new_group_form_submit").click(post_new_group_form)

}

route_to_all_categories = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    console.log("all categories")
    let content = categories_component.format("ALL CATEGORIES", "Add New Category", "open_new_category_model()")
    content = $.parseHTML(content)
    $("#router_outlet").append(content)
    for (let cat of list_all_categories) {
        const url = render_random_img(cat.name)

        const cat_ele = $.parseHTML(category_card.format(cat.name, cat.name, cat.id, url))
        $(".container_for_categories").append(cat_ele)
    }
}

route_to_view_all_groups = () => {
    console.log("view all was clicked")
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()

    //get data from server or from browser
    all_groups = list_all_groups

    //render
    let line_all_recent_groups = ""
    all_groups.forEach(G => {
        console.log(G)
        line_all_recent_groups += get_group_row_element_for_all_group_list(G)
    });
    console.log(line_all_recent_groups)

    //render
    $("#router-outlet").html(table_of_groups.format("All Groups", "Add New Group","all",  "route_to_create_new_group()"))
    $("#rows_of_recent_groups_table_all").html(line_all_recent_groups)

}

route_to_view_your_groups = () => {

}

route_to_groups_for_category = (cat_id) => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    console.log("cate", cat_id)
}

post_new_group_form = (e) =>{
    // $("#loader").css('display', 'block')
    e.preventDefault(); // avoid to execute the actual submit of the form

    
        $.ajax({ 
          type: "POST",
          url: "/submit_new_group", // it's the URL of your component B
          data: $("#frm1").serialize(), // serializes the form's elements
          success: function(data)
          {
            route_to_home_page()

            // $("#loader").css('display', 'none')
           // show_alert("success", "You have created a new purchasing group!")
              console.log("post", data)

            // show the data you got from B in result div
            //$("#result").html(data);
          }
        });
    //   });
}

async function route_to_group_details(group_id) {
    //get group details from server , includes imgs
    num_of_subscribers = 8 //@TODO
    group = list_all_groups.find(G => G.group_id  == group_id)
    imgs_collection1 = $("#group_details_imgs_of_product_1")
    imgs_collection2 = $("#group_details_imgs_of_product_1")

    //render
    $("#router-outlet").addClass("hidden")

    console.log(group)
    $("#product_details_num_of_subscibers").html(group.num_of_subscribers)
    $("#short_description_of_group").html(group.group_name)//item_name)
    $("#brand_of_group_in_details").html(group.category)
    $("#range_sum_for_group_product").html("max sum : " + group.max_price + "$")
    $("#long_decription_of_group").html("description: \n" + group.description_group)
    $("#group_duedate").html(group.end_data)
    $("#group_manager").html(group.manager)
    $("#group_details").removeClass("hidden")

    for(let i = 1; i < 7; i ++){
        let url = render_random_img_by_category(group.category, i)
    }
}



const render_img = _.template(`<img src="<%=img_path%>" alt="">`);


open_new_category_model = () => {

}

open_new_group_model  = () => {

}


//UTILS
compare_by_date = (a, b) => {
    return a.end_data - b.end_data
}

get_category_name_by_id = (category_id) => {
    return category_id;
}

function render_random_img(category_str) {
    return "https://dalicanvas.co.il/wp-content/uploads/2019/01/%D7%A0%D7%95%D7%A3-%D7%9C%D7%94%D7%A8%D7%99%D7%9D-8.jpg"
}
function render_random_img_by_category(category_str, num) {
    url = `https://source.unsplash.com/600x800/?${category_str}`

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function (e) {
        if (xhr.status == 200 && xhr.readyState == 4) {
            console.log(xhr.responseURL)
            let img1 = $("#img1_" + num)
            img1.attr("src", xhr.responseURL)
            let img2 = $("#img2_" + num)
            img2.attr("src", xhr.responseURL)
            console.log(img1.attr("src"), img2)
            return xhr.responseURL
            // console.log("#" + img_id)
            // $("#" + img_id).attr("src", img_url)
            // console.log(document.getElementById(img_id),   img_id)
            // new_item = $("#" + img_id).clone()
            // $("#container_for_categories").append(new_item)

        }
    }
    xhr.open("GET", url, true);
    xhr.send();
}


String.prototype.format = function () {
    a = this;
    for (k in arguments) {
        a = a.replaceAll("{" + k + "}", arguments[k])
    }
    return a
}

show_alert  = (status, msg) => {
    $("#show_alert_success").on('click', function() {
        swal( status + "!", msg,  status);
    });
    $( "#show_alert_success" ).trigger( "click" )
}