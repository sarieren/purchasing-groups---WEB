const table_of_groups = `
<!--Main Content-->
<!--Groups latest-->
<div class="mt-4 mb-4 bg-white border shadow lh-sm">
    <!--Recent Sales-->
    <div class="product-list">

        <div class="row mb-0 px-3 pt-3">
            <div class="col-sm-8 pt-2">
                <h6 class="mb-4 bc-header">{0}</h6>
            </div>
            <div class="col-sm-4 text-right pb-3">
                <div class="pull-right mr-3 btn-order-bulk">
                    <button class="btn btn-theme btn-round" id="btn_view_all_groups_in_list" onclick="{3}">{1}</button>
                </div>

                <div class="clearfix"></div>
            </div>
        </div>

        <div class="table-responsive product-list">

            <table class="table mt-0 " id="productList">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Subscibers</th>
                        <th>Category</th>
                        <th>Due Date</th>
                    </tr>
                </thead>
                <tbody id="rows_of_recent_groups_table_{2}"></tbody>

            </table>
        </div>
    </div>
    <!--/Recent sales-->
</div>
`

const main_content = `
<div class="row mt-1">

    <div class="col-sm-12 col-md-4">
        <!--Analytics-->
        <div class="bg-white border shadow mb-4 mt-4">
            <div class="media p-4">
                <div class="align-self-center mr-3 rounded-circle notify-icon_2 bg-white">
                    <i class="fa fa-globe text-theme"></i>
                </div>
                <div class="media-body pl-2">
                    <h3 class="mt-0 mb-0"><strong id="num_of_app_visitors">{num of app
                            visitors}</strong></h3>
                    <p><small class="bc-description text-theme">TOTAL VISITORS</small></p>
                </div>
            </div>
        </div>

        <div class="bg-white border shadow mb-4">
            <div class="media p-4">
                <div class="align-self-center mr-3 rounded-circle notify-icon_2 bg-white">
                    <i class="fa fa-heart-o text-danger"></i>
                </div>
                <div class="media-body pl-2">
                    <h3 class="mt-0 mb-0"><strong
                            id="num_of_visitors_likes">{num_of_visitors_likes}</strong></h3>
                    <p><small class="bc-description text-danger">VISITORS LIKE US</small></p>
                </div>
            </div>
        </div>

        <div class="bg-white border shadow">
            <div class="media p-4">
                <div class="align-self-center mr-3 rounded-circle notify-icon_2 bg-white">
                    <i class="fa fa-lightbulb text-success"></i>
                </div>
                <div class="media-body pl-2">
                    <h3 class="mt-0 mb-0"><strong
                            id="number_of_groups_created">{number_of_groups_created}</strong></h3>
                    <p><small class="text-success bc-description">GROUPS</small></p>
                </div>
            </div>
        </div>
        <!--/Analytics-->

    </div>


    <!--CONTACT FORM-->
    <div class="col-sm-12 col-md-8">
        <!--Default bootstrap 4 validation-->
        <div class="mt-1 mb-4 p-3 button-container bg-white border shadow-sm">
            <h3 class="mb-2">Contact Us</h3>

            <form class="needs-validation" id="contact_form" novalidate action="#">
                <div class="form-row">
                    <div class="col-md-6 col-sm-12 mb-2">
                        <label for="validationCustom01">Name or User Name <span
                                class="text-danger">*</span></label>
                        <input type="text" class="form-control" id="validationCustom01" placeholder=""
                            required>
                        <div class="valid-feedback">
                            Looks good!
                        </div>
                    </div>

                    <div class="col-md-6 col-sm-12 mb-2">
                        <label for="validationCustomUsername">Mail <span
                                class="text-danger">*</span></label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <span class="input-group-text" id="inputGroupPrepend">@</span>
                            </div>
                            <input type="text" class="form-control" id="validationCustomUsername"
                                placeholder="" aria-describedby="inputGroupPrepend" required>
                            <div class="invalid-feedback">
                                Please choose a mail address.
                            </div>
                        </div>
                    </div>

                </div>

                <div class="form-group form-row mt-4 ">
                    <label for="validationTxtArea">Massege: <span class="text-danger">*</span></label>
                    <div class="col-sm-12 col-md-12 mb-2 mt-1">
                        <textarea id="validationTxtArea" class="form-control" name="text"></textarea>
                    </div>
                </div>



                <div class="row">

                    <div class="col-sm-6 mb-2">
                        <label for="">optional file input</label>
                        <div class="custom-file">
                            <input type="file" class="custom-file-input" id="customFile">
                            <label class="custom-file-label" for="customFile">Choose file...</label>
                        </div>
                    </div>
                </div>


                <button class="btn btn-primary btn-lg mt-2" type="submit">Send</button>
            </form>
        </div>
        <!--/Default bootstrap validation-->
    </div>
</div>

`




 const get_group_row_element_for_all_group_list = _.template(`
<tr id="group_line_<%= group_id %>_<%= category %>" class="group_row_in_table pl-3 pr-3" onclick="route_to_group_details(<%= group_id %>)">
<td class="align-middle px-4"><%= group_name %></td>
<input class="id_of_group" value="<%= group_id %>" style="display:hidden"/>
<td class="align-middle">
    <div class="customers pt-3">
        
        <span class="customer-circle end text-light text-center pt-2 mt-4"><i class="fa fa-user "></i></span>
        <span class="customer-circle end text-light text-center pt-2 mt-4"><i class="fa fa-user"></i></span>
        <span id="amount_of_subscribers_to_group_in_list" class="customer-circle end text-light text-center pt-2 mt-4"><%= num_of_subscibers %></span>
    </div>
</td>
<td class="align-middle">
    <button class="btn-outline-theme btn-round">
    <%= category_str %>
    </button>
</td>
<td class="align-middle">
    <h4><%= end_date %> </h4>
</td>
</tr>`);





const categories_component = `
<div class="col-sm-12 col-xs-12 content pt-3 pl-0">
<div class="row mt-3">
    <div class="col-sm-12">
        <!--Cards with image-->
        <div class="mt-1 mb-3 button-container">
            <div class="card-columns container_for_categories">
                

            </div>
        </div>
        <!--/Cards with image-->

    </div>
</div>



</div>
`




const category_card = `
                
                <div class=" mb-3 ">
                    <div class="card" id="category_{2}" onclick="route_to_groups_for_category({2})">
                        <img class="card-img-top" id=category_img_{2}" src="{3}" alt="category image cap">
                        <div class="card-body">
                            <h5 class="card-title">{0}</h5>
                            <p class="card-text">{1}</p>
                            <!--<a href="#" class="btn btn-theme text-white">Foward</a> -->
                        </div>
                    </div>
                </div>
                
`



const new_group_form = _.template(`
<div class="col-sm-12 col-xs-12 content pt-3 pl-0">
<h5 class="mb-0" ><strong>new group</strong></h5>
<span class="text-secondary">groups <i class="fa fa-angle-right"></i> add a new group</span>

<div class="row mt-3">
    <div class="col-sm-12">
        <!--Blank Page-->
        <div class="mt-1 mb-3 p-3 button-container border bg-white">
            <h6 class="mb-3">Blank page</h6>
            <form id="frm1"> <!-- action="/submit_new_group" method="post">-->
            
                group name: <input type="text" name="group_name"required><br>
                item name: <input type="text" name="item_name" required ><br>
                max price: <input type="number" name="max_price" required><br>
                
                category: <select class="px-2" name="category" id="category" required>
                   <!-- {% for category in categories %}
                        <option value={{category}}>{{category}}</option>
                    {%endfor%}-->

                    <% _.each( categories, function( category ){ %>
                        <option class="px-2" value=<%=category.name %>> <%=category.name %></option>    
                    <% }); %>
                </select><br>
                
                end time for purchas:	day: <input type="date" id="date_" name="end_time_day" min="2021-01-01" required>	time: <input type="time" name="end_time_time" required><br>
                
                group description: <br><textarea  name="group_description" cols="60" rows="5"></textarea>
                <br>
                <input type="submit" value="submit" id="new_group_form_submit">
            </form>
            
        </div>
        <!--/Blank Page-->

    </div>
</div>



</div>
`)



const forum_msg2 = `
                <div class="tab-pane fade show active p-3" id="custom-home" role="tabpanel"
                        aria-labelledby="nav-home" id="{0}">

                        <!--Single feed-->
                        <div class="feed-single mb-3">
                            <div class="media">
                                <img class="mr-3 rounded-circle" height="40px" width="40px"
                                    src="{2}" alt="Generic placeholder image">
                                <div class="media-body">
                                    <h6 class="mt-1">{0}
                                        <small class="text-muted pl-3"><i class="fa fa-clock"></i>{4}</small>

                                        <p class="clearfix"></p>
                                    </h6>


                                    <p>{1}</p>

                                    <div class="feed-footer mt-3">
                                        <p class="pr-3 blue-text"><i class="fa fa-heart"></i> {3} LIKE  </p>

                                        <p class="clearfix"></p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--/Single feed-->
                        <hr>


                    

                    </div>
`


const forum_msg = `
<div class="tab-pane fade show active p-3" id="custom-home" role="tabpanel" aria-labelledby="nav-home" id="{0}">

<!--Single feed-->
<div class="feed-single mb-3 row">
    <div class="col-sm-12 col-md-3 msg-meta">
        <span id=""
            class="user-letter-msg customer-circle end text-light text-center pt-2 mt-4 user_img_letter ml-3">{6}</span>
        <h5 class="mt-1" style="font-weight: 600;">{0}</h5>
    </div>
    <div class="col-sm-12 col-md-8 msg-data">
        <h6 class="mt-1">
            <small class="text-muted pl-3"><i class="fa fa-clock"></i>{4}</small>
            <hr>
        </h6>


        <div>{1}</div>

        <div class="feed-footer px-1">
            <h6 class="mt-1">
                <hr>
            </h6>
            <div>
                <a href="" class=" blue-text" onclick="add_like_for_group({5})">Like <i
                        class="fa-thumbs-up fa"></i></a>
                <a href="" class="pr-3 blue-text"><i class="fa fa-heart"></i> {3} LIKES </a>
            </div>

        </div>
        <!-- </div> -->
    </div>
</div>
<!--/Single feed-->
<hr>


</div>
`