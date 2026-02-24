/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class ShopifyConnectorAction extends Component {
    static template = "dasolo_shopify_connector.ShopifyConnectorAction";

    setup() {
        this.iframeSrc = "https://odoo-shopify-connector.dasolo.ai/login";
    }
}

registry.category("actions").add("dasolo_shopify_connector_action", ShopifyConnectorAction);
