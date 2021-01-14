$(document).ready(() => {
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

//get groups and categories data from server
list_all_groups = []
list_all_categories = []
cat_ob = {}
all_groups_elements = []
all_categories_element = []
user_groups_id = []
user_name = ""
num_of_app_visitors = 999
num_of_visitors_likes = 567
number_of_groups_created = 100

get_user_data = () => {

    return $.get("/users/" + user_name, (res) => {
        res = JSON.parse(res)
        // user_mail = res.user_mail
        user_img_path = "assets\\img\\client-img4.png"
        user_img_letter = user_name[0]
        $("#user_name").text(user_name)
        $("#user_mail").text(res["user_mail"])
        // $(".user_img_path").attr("src", user_img_path)
        $(".user_img_letter").text(user_img_letter)

    })

}


get_categories_data = () => {
    return $.get("/categories", (data, status) => {
        list_all_categories = JSON.parse(data)
        list_all_categories.forEach(cat => {
            cat_ob[cat.id] = cat.name
            render_random_img_by_category(cat.name, cat.id)


        })
    })


}


get_groups_data = () => {
    return $.get("/groups", (data) => {

        list_all_groups = JSON.parse(data)
        list_all_groups.sort(compare_by_date);
    })


}


get_users_group_id = (username) => {
    return $.get("/purchasers/" + username, (res) => {
        user_groups_id = Array.from(JSON.parse(res))
    })


}

init_page = () => {
    loading()
    //get user and main data from server
    user_name = document.cookie.split("username=")[1]
    $("#loader").css('display', 'block')
    $.when(
        get_groups_data(),
        get_user_data(),
        get_categories_data(),
        get_users_group_id(user_name)
    ).then(() => {

        $("#group_details").addClass("hidden")
        $("#router-outlet").removeClass("hidden")

        content = $.parseHTML(categories_component + main_content)
        $("#router-outlet").append(content)
        $("#num_of_app_visitors").text(num_of_app_visitors)
        $("#num_of_visitors_likes").text(num_of_visitors_likes)
        $("#number_of_groups_created").text(number_of_groups_created)

        temp_cat_str = ""
        for (let cat of list_all_categories) {
            temp_cat_str += category_card.format(cat.name, cat.name, cat.id, cat_ob[cat.id + "_urls"][Math.floor(Math.random() * cat_ob[cat.id + "_urls"].length)])
        }
        all_categories_element = $.parseHTML(temp_cat_str)
        filter_and_add_list_elements_to_father_element(".container_for_categories", all_categories_element, () => true)

        temp_group_str = ""
        for (let G of list_all_groups) {
            G["category_str"] = cat_ob[G.category]
            temp_group_str += get_group_row_element_for_all_group_list(G)
        }
        all_groups_elements = $.parseHTML(temp_group_str)

        //event listeners
        $("#btn_view_all_groups_in_list").click(() => route_to_view_all_groups())
        $("#btn_subscribe").click((e) => subscribe_user_to_group(e.currentTarget, e))
        $("#link_to_user_profile").click(() => console.log("clicked on profile"))
        $("#link_show_groups_by_category").click(() => route_to_all_categories)
        $("#link_show_all_groups").click(route_to_view_all_groups)
        $("#link_to_your_groups").click(route_to_view_your_groups)
        $("#link_to_create_new_group").click(route_to_create_new_group)

        $("#logo").click(route_to_home_page)
        stop_load()
    });

}

loading = () => $(".loader-wrapper").css('display', 'block')
stop_load = () => $(".loader-wrapper").css('display', 'none')


route_to_home_page = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    content = $.parseHTML(categories_component + main_content)
    $("#router-outlet").append(content)
    // $(".user_img_path").attr("src", user_img_path)
    $("#num_of_app_visitors").text(num_of_app_visitors)
    $("#num_of_visitors_likes").text(num_of_visitors_likes)
    $("#number_of_groups_created").text(number_of_groups_created)
    filter_and_add_list_elements_to_father_element(".container_for_categories", all_categories_element, () => true)

}

subscribe_user_to_group = (target) => {
    //get user and main data from cookie
    user_name = document.cookie.split("username=")[1]

    data_dict = {
        "group_id": target.value,
        "user_name": user_name
    }
     loading()

    $.ajax({
        type: "POST",
        url: "/purchasers", // it's the URL of your component B
        data: data_dict,
        success: function (data) {
            show_alert("success", "You have been to the purchasing group")
            user_groups_id.push(data["group_id"])
            stop_load()
        },
        error: function (data) {
            show_alert("error", "there was a problem with the subscription, please try again")
            stop_load()
        }
    });
}



route_to_create_new_group = () => {
    //render new group form
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()
    let content = $.parseHTML(new_group_form({
        "categories": list_all_categories
    }))
    $("#router-outlet").append(content)
    date = format_date(new Date())
    $('#date_').attr("min", date)

    $(document).on('submit', '#frm1', post_new_group_form)

}

route_to_view_all_groups = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()

    //render
    $("#router-outlet").html(table_of_groups.format("All Groups", "Add New Group", "all", "route_to_create_new_group()"))
    filter_and_add_list_elements_to_father_element("#rows_of_recent_groups_table_all", all_groups_elements, () => true)
}

route_to_view_your_groups = () => {
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()

    //render
    $("#router-outlet").html(table_of_groups.format("My Groups", "Add New Group", "user", "route_to_create_new_group()"))
    filter_and_add_list_elements_to_father_element("#rows_of_recent_groups_table_user", all_groups_elements, filtered_users_group)
}

filtered_users_group = (item) => {
    
    if (item.nodeType == 3) return false
    group_id = item.id.split("_")[2]
    return user_groups_id.indexOf(parseInt(group_id)) >= 0
}




route_to_groups_for_category = (cat_id) => {
    // e.stopPropagation();

    // cat_id = 
    $("#group_details").addClass("hidden")
    $("#router-outlet").removeClass("hidden")
    $("#router-outlet").empty()

    filtered_category_group = (item) => {
        if (item.nodeType == 3)
            return false
        return item.id.split("_")[3] == "" + cat_id
        
    }
    $("#router-outlet").html(table_of_groups.format("Groups for Category " + cat_ob[cat_id], "Add New Group", "cat", "route_to_create_new_group()"))
    filter_and_add_list_elements_to_father_element("#rows_of_recent_groups_table_cat", all_groups_elements, filtered_category_group)
    
}

post_new_group_form = (e) => {
    // $("#loader").css('display', 'block')
    e.preventDefault(); // avoid to execute the actual submit of the form
    loading()

    $.ajax({
        type: "POST",
        url: "/submit_new_group", // it's the URL of your component B
        data: $("#frm1").serialize(), // serializes the form's elements
        success: function (data) {
            list_all_groups.push({
                group_id: data.id_,
                group_name: data.group_name,
                num_of_subscibers: data.num_of_subscibers,
                item_name: data.item_name,
                max_price: data.max_price,
                manager: data.manager,
                category: cat_ob[data.category_id],
                end_data: data.end_data,
                description_group: data.description_group

            })

            route_to_home_page()
            stop_load()
            show_alert("success", "You have created a new purchasing group!")
        },
        error: function (data) {
            stop_load()
            show_alert("error", "there was a problem with adding a new group, please try again")
        }
    });
}

async function route_to_group_details(group_id) {
    //get group details from server , includes imgs
    group = list_all_groups.find(G => G.group_id == group_id)
    urls = cat_ob[group.category + "_urls"]
    imgs_collection1 = $("#group_details_imgs_of_product_1")
    imgs_collection2 = $("#group_details_imgs_of_product_1")
    for (let i = 1; i < 7; i++) {
        url = urls[Math.floor(Math.random() * urls.length)]
        $("#img1_" + i).attr("src", url)
        $("#img2_" + i).attr("src", url)
    }

    //render
    $("#router-outlet").addClass("hidden")
    //add value for subscirbe btn - to get in subscribe time
    $("#btn_subscribe").attr("value", group_id)

    $("#product_details_num_of_subscibers").html(group.num_of_subscibers)
    $("#short_description_of_group").html(group.group_name) //item_name)
    $("#group_id_for_forum").attr("value", group_id)
    $("#brand_of_group_in_details").html(cat_ob[group.category])
    $("#range_sum_for_group_product").html("max sum : " + group.max_price + "$")
    $("#long_decription_of_group").html("description: \n" + group.description_group)
    $("#group_duedate").html(group.end_date)
    $("#group_manager").html(group.manager)
    $("#group_details").removeClass("hidden")




    msgs = []
    $.get("/forums/" + group_id, (res) => {

        msgs = JSON.parse(res)

        user_img_path = "assets\\img\\John-doe.png"
        //get forum msgs 
        // forum = $("#forum_of_group")
        if (typeof (msgs) == Array) {
            msgs.forEach(M => {
                forum = $("#forum_of_group")
                gid = M['group_id']
                uname = M['user_name']
                msg = M['message_']
                likes = M['count_like']
                time = M['end_time'] + ", " + M['end_time']
                let msg_ele = $.parseHTML(forum_msg.format(uname, msg, user_img_path, likes, time))
                forum.append(msg_ele)
            });
        }
    })

    $(document).on('submit', '#new_msg', createMsg)


}

function createMsg(e) {
    e.preventDefault()
    group_id = $("#group_id_for_forum").attr("value")


    $.post("/forums", {
            groupId: group_id,
            msg: $("#msg").attr("value")
        },
        function (returnedMsgs) {
            returnedMsgs = JSON.parse(returnedMsgs)
            forum = $("#forum_of_group")
            gid = returnedMsgs.group_id
            uname = returnedMsgs.user_name
            msg = returnedMsgs['message_']
            likes = returnedMsgs['count_like']
            time = returnedMsgs['end_date'] + ", " + returnedMsgs['end_time']
            let msg_ele = $.parseHTML(forum_msg.format(uname, msg, user_img_path, likes, time))
            forum.append(msg_ele)
            msg: $("#msg").attr("value", "")

        });

}

const render_img = _.template(`<img src="<%=img_path%>" alt="">`);


//UTILS
compare_by_date = (a, b) => {
    return a.end_data - b.end_data
}

get_category_name_by_id = (category_id) => {
    return category_id;
}


function render_random_img_by_category(category_str, cat_id) {
    url = `https://pixabay.com/api/?key=19156012-fe856b2884e74c41ff3f38122&q=${category_str}&image_type=photo`
    res = $.ajax({
        async: false,
        url: url
    }).done((res) => {

        cat_ob[cat_id + "_urls"] = res["hits"].map(U => U["webformatURL"])
    })
}




String.prototype.format = function () {
    a = this;
    for (k in arguments) {
        a = a.replaceAll("{" + k + "}", arguments[k])
    }
    return a
}

show_alert = (status, msg) => {
    $("#show_alert_success").on('click', function () {
        swal(status + "!", msg, status);
    });
    $("#show_alert_success").trigger("click")
}




format_date = (date) => {
    var dd = date.getDate()
    var mm = date.getMonth() + 1;
    var yyyy = date.getFullYear();
    if (dd < 10) {
        dd = '0' + dd;
    }
    if (mm < 10) {
        mm = '0' + mm;
    }
    return yyyy + '-' + mm + '-' + dd;
}

filter_and_add_list_elements_to_father_element = (father_ele_name, child_list_ele, filter_func) => {
    filterd_list = child_list_ele.filter(filter_func)
    $(father_ele_name).append(filterd_list)
}