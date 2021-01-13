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
<tr id="group_line_<%= group_id %>" class="group_row_in_table pl-3 pr-3" onclick="route_to_group_details(<%= group_id %>)">
<td class="align-middle px-4"><%= group_name %></td>
<td class="align-middle">
    <div class="customers pt-3">
        
        <span class="customer-circle end text-light text-center pt-2 mt-4"><i class="fa fa-user "></i></span>
        <span class="customer-circle end text-light text-center pt-2 mt-4"><i class="fa fa-user"></i></span>
        <span id="amount_of_subscribers_to_group_in_list" class="customer-circle end text-light text-center pt-2 mt-4"><%= num_of_subscibers %></span>
    </div>
</td>
<td class="align-middle">
    <button class="btn-outline-theme btn-round">
    <%= category %>
    </button>
</td>
<td class="align-middle">
    <div class="progress" style="height: 5px;">
        <div class="progress-bar bg-theme" role="progressbar" aria-valuenow="50"
            style="width: 85%" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
</td>
</tr>`);






create_new_group = `
<div class="col-sm-9 col-xs-12 content pt-3 pl-0">
<h5 class="mb-0" ><strong>Form wizard</strong></h5>
<span class="text-secondary">Dashboard <i class="fa fa-angle-right"></i> form wizard</span>

<div class="row mt-3">
    <div class="col-sm-12">
        <!--Form wizard-->
        <div class="mt-1 mb-3 p-3 button-container bg-white border shadow-sm">
            <h6>Wizard with validation</h6>
            <p>Wizard gives you a possibility to use separate form into steps</p>
            
            <div class="wizard-container">
                <div class="card wizard-card" data-color="theme" id="wizardProfile">
                    <form action="" method="">
                    <!--        You can switch " data-color="orange" "  with one of the next bright colors: "blue", "green", "orange", "red", "azure"          -->

                        <div class="wizard-header text-center">
                            <h3 class="wizard-title">Create your profile</h3>
                            <p class="category">This information will let us know more about you.</p>
                        </div>

                        <div class="wizard-navigation">
                            <div class="progress-with-circle">
                                    <div class="progress-bar" role="progressbar" aria-valuenow="1" aria-valuemin="1" aria-valuemax="3" style="width: 21%;"></div>
                            </div>
                            <ul>
                                <li>
                                    <a href="#about" data-toggle="tab">
                                        <div class="icon-circle">
                                            <i class="ti-user"></i>
                                        </div>
                                        About
                                    </a>
                                </li>
                                <li>
                                    <a href="#account" data-toggle="tab">
                                        <div class="icon-circle">
                                            <i class="ti-settings"></i>
                                        </div>
                                        Work
                                    </a>
                                </li>
                                <li>
                                    <a href="#address" data-toggle="tab">
                                        <div class="icon-circle">
                                            <i class="ti-map"></i>
                                        </div>
                                        Address
                                    </a>
                                </li>
                            </ul>
                        </div>
                        <div class="tab-content">
                            <div class="tab-pane" id="about">
                                <div class="row">
                                    <div class="col-sm-10 offset-sm-1">
                                        <h6 class="info-text text-center"> Please tell us more about yourself.</h6>
                                        <div class="row">
                                            <div class="col-sm-4">
                                                <div class="picture-container">
                                                    <div class="picture">
                                                        <img src="assets\img\default-avatar.jpg" class="picture-src" id="wizardPicturePreview" title="" />
                                                        <input type="file" id="wizard-picture">
                                                    </div>
                                                    <h6>Choose Picture</h6>
                                                </div>
                                            </div>

                                            <div class="col-sm-8">
                                                <div class="form-group">
                                                    <label>First Name <small>(required)</small></label>
                                                    <input name="firstname" type="text" class="form-control" placeholder="Andrew...">
                                                </div>
                                                <div class="form-group">
                                                    <label>Last Name <small>(required)</small></label>
                                                    <input name="lastname" type="text" class="form-control" placeholder="Smith...">
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="col-sm-10 offset-sm-1">
                                        <div class="form-group">
                                            <label>Email <small>(required)</small></label>
                                            <input name="email" type="email" class="form-control" placeholder="andrew@creative-tim.com">
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="tab-pane" id="account">
                                <h5 class="info-text"> What are you doing? (checkboxes) </h5>
                                    <div class="row">
                                        <div class="col-sm-4">
                                            <div class="choice" data-toggle="wizard-checkbox">
                                                <input type="checkbox" name="jobb" value="Design">
                                                <div class="card card-checkboxes card-hover-effect">
                                                    <i class="ti-paint-roller"></i>
                                                    <p>Design</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-sm-4">
                                            <div class="choice" data-toggle="wizard-checkbox">
                                                <input type="checkbox" name="jobb" value="Code">
                                                <div class="card card-checkboxes card-hover-effect">
                                                    <i class="ti-pencil-alt"></i>
                                                    <p>Code</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-sm-4">
                                            <div class="choice" data-toggle="wizard-checkbox">
                                                <input type="checkbox" name="jobb" value="Develop">
                                                <div class="card card-checkboxes card-hover-effect">
                                                    <i class="ti-star"></i>
                                                    <p>Develop</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="tab-pane" id="address">
                                    <div class="row">
                                        <div class="col-sm-12">
                                            <h5 class="info-text"> Are you living in a nice area? </h5>
                                        </div>
                                        <div class="col-sm-7 col-sm-offset-1">
                                            <div class="form-group">
                                                <label>Street Name</label>
                                                <input type="text" class="form-control" placeholder="5h Avenue">
                                            </div>
                                        </div>
                                        <div class="col-sm-3">
                                            <div class="form-group">
                                                <label>Street Number</label>
                                                <input type="text" class="form-control" placeholder="242">
                                            </div>
                                        </div>
                                        <div class="col-sm-5 col-sm-offset-1">
                                            <div class="form-group">
                                                <label>City</label>
                                                <input type="text" class="form-control" placeholder="New York...">
                                            </div>
                                        </div>
                                        <div class="col-sm-5">
                                            <div class="form-group">
                                                <label>Country</label><br>
                                                <select name="country" class="form-control">
                                                    <option value="Afghanistan"> Afghanistan </option>
                                                    <option value="Albania"> Albania </option>
                                                    <option value="Algeria"> Algeria </option>
                                                    <option value="American Samoa"> American Samoa </option>
                                                    <option value="Andorra"> Andorra </option>
                                                    <option value="Angola"> Angola </option>
                                                    <option value="Anguilla"> Anguilla </option>
                                                    <option value="Antarctica"> Antarctica </option>
                                                    <option value="...">...</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="wizard-footer">
                                <div class="pull-right">
                                    <input type='button' class='btn btn-next btn-fill btn-theme btn-wd' name='next' value='Next' />
                                    <input type='button' class='btn btn-finish btn-fill btn-theme btn-wd' name='finish' value='Finish' />
                                </div>

                                <div class="pull-left">
                                    <input type='button' class='btn btn-previous btn-default btn-wd' name='previous' value='Previous' />
                                </div>
                                <div class="clearfix"></div>
                            </div>
                        </form>
                    </div>
                </div> <!-- wizard container -->
            
        </div>
        <!--/Form wizard-->
    </div>
</div>


</div>
`



const categories_component = `
<div class="col-sm-12 col-xs-12 content pt-3 pl-0">
<div class="row">
    <div class="row mb-5 pt-3 justify-content-around">
        <h6 class="mb-4 bc-header left_float">{0}</h6>
        <button class="btn btn-theme btn-round right_float" id="btn_view_all_categories_in_list" onclick="{2}">{1}</button>
    </div>
</div>

<div class="row mt-3">
    <div class="col-sm-12">
        <!--Cards with image-->
        <div class="mt-1 mb-3 button-container">
            <div class="row container_for_categories">
                

            </div>
        </div>
        <!--/Cards with image-->

    </div>
</div>



</div>
`




const category_card = `
                <div class="col-md-3 col-sm-6 mb-3">
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
<div class="col-sm-9 col-xs-12 content pt-3 pl-0">
<h5 class="mb-0" ><strong>new group</strong></h5>
<span class="text-secondary">groups <i class="fa fa-angle-right"></i> add a new group</span>

<div class="row mt-3">
    <div class="col-sm-12">
        <!--Blank Page-->
        <div class="mt-1 mb-3 p-3 button-container border bg-white">
            <h6 class="mb-3">Blank page</h6>
            <form id="frm1"> <!-- action="/submit_new_group" method="post">-->
            
                group name: <input type="text" name="group_name"><br>
                item name: <input type="text" name="item_name"><br>
                max price: <input type="number" name="max_price"><br>
                
                category: <select class="px-2" name="category" id="category">
                   <!-- {% for category in categories %}
                        <option value={{category}}>{{category}}</option>
                    {%endfor%}-->

                    <% _.each( categories, function( category ){ %>
                        <option class="px-2" value=<%=category.name %>> <%=category.name %></option>    
                    <% }); %>
                </select><br>
                
                end time for purchas:	day: <input type="date" name="end_time_day">	time: <input type="time" name="end_time_time"><br>
                
                group description: <br><textarea  name="group_description" cols="60" rows="5"></textarea>
                <br>
                <input type="button" value="submit" id="new_group_form_submit">
            </form>
            
        </div>
        <!--/Blank Page-->

    </div>
</div>



</div>
`)