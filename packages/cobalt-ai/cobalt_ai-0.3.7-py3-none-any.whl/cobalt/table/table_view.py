# Copyright (C) 2023-2024 BlueLightAI, Inc. All Rights Reserved.
#
# Any use, distribution, or modification of this software is subject to the
# terms of the BlueLightAI Software License Agreement.

from typing import List, Optional, Tuple
from uuid import UUID

import ipyvuetify as v
import traitlets


class TableView(v.VuetifyTemplate):
    workspace_id = traitlets.Unicode(allow_none=True).tag(sync=True)
    headers = traitlets.List([]).tag(sync=True, allow_null=True)
    items = traitlets.List([]).tag(sync=True, allow_null=True)
    footer_props = traitlets.Dict({}).tag(sync=True)

    def __init__(
        self,
        workspace_id: Optional[UUID] = None,
        image_columns: Optional[List[dict]] = None,
        html_columns: Optional[List[str]] = None,
        image_size: Tuple[int, int] = (80, 80),
        **kwargs,
    ):
        if workspace_id is not None:
            self.workspace_id = str(workspace_id)
        if image_columns is None:
            image_columns = []
        if html_columns is None:
            html_columns = []

        self.image_columns = image_columns
        self.html_columns = html_columns
        self.image_height, self.image_width = image_size
        super().__init__(**kwargs)

    def _generate_column_templates(self) -> str:
        image_template = "\n".join(
            [
                f"""
            <template v-slot:item.{img_col["column_name"]}="props">
            <v-img
                :src="props.item.{img_col["column_name"]}"
                height="{self.image_height}"
                width="{self.image_width}"
            >
            </v-img>
            </template>"""
                for img_col in self.image_columns
            ]
        )

        html_template = "\n".join(
            [
                f"""
            <template v-slot:item.{text_col}="props">
            <div v-html="props.item.{text_col}"></div>
            </template>"""
                for text_col in self.html_columns
            ]
        )

        return image_template + "\n" + html_template

    @traitlets.default("template")
    def _template(self):
        template = (
            """
            <template>
            <v-data-table
                :items="items"
                :headers="headers"
                :footer-props="footer_props"
                :data-table-id="tableId"
                @update:items-per-page="onItemsPerPageChange"
            >"""
            + self._generate_column_templates()
            + """
        </v-data-table>
        </template>

        <script>
          export default {
              data() {
                return {
                  tableId: '',
                };
              },
              mounted() {
                this.$nextTick(() => {
                  if (this.workspace_id) {
                    this.tableId = 'table-' + this.workspace_id;

                    // Ensure DOM is fully updated
                    this.$nextTick(() => {
                      const tableElements = document.querySelectorAll(
                        `[data-table-id="${this.tableId}"]`
                      );

                      const storedItemsPerPage = sessionStorage.getItem(
                        `items_per_page_${this.tableId}`
                      ) || '10';

                      tableElements.forEach((tableElement) => {
                        const footerSelect = tableElement.querySelector(
                          '.v-data-footer__select'
                        );
                        if (footerSelect) {
                          const itemsPerPageInput = footerSelect.querySelector(
                            'input[aria-label="$vuetify.TableView.itemsPerPageText"]'
                          );
                          const itemsPerPageDisplay = footerSelect.querySelector(
                            '.v-select__selection--comma'
                          );

                          if (itemsPerPageInput) {
                            itemsPerPageInput.value = storedItemsPerPage;

                            // Trigger the change event to notify Vue
                            const event = new Event('input', { bubbles: true });
                            itemsPerPageInput.dispatchEvent(event);
                          }

                          if (itemsPerPageDisplay) {
                            itemsPerPageDisplay.innerText = storedItemsPerPage;
                          }
                        }
                      });
                    });
                  }
                });
              },
              methods: {
                onItemsPerPageChange(itemsPerPage) {
                  // Manually update the text because menu styles set the default
                  // option to the first element. If you select this element,
                  // the inner text won't change.

                  if (this.workspace_id) {
                    this.$nextTick(() => {
                      const tableElements = document.querySelectorAll(
                        `[data-table-id="${this.tableId}"]`
                      );

                      sessionStorage.setItem(
                        `items_per_page_${this.tableId}`, itemsPerPage
                      );

                      tableElements.forEach((tableElement) => {
                        const footerSelect = tableElement.querySelector(
                          '.v-data-footer__select'
                        );
                        if (footerSelect) {
                          const itemsPerPageDisplay = footerSelect.querySelector(
                            '.v-select__selection--comma'
                          );
                          if (itemsPerPageDisplay) {
                            itemsPerPageDisplay.innerText = itemsPerPage;
                          }
                        }
                      });
                    });
                  }
                }
              }
            };
        </script>
        """
        )
        return template
